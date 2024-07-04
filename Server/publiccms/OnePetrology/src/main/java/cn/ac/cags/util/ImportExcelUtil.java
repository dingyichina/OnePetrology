package cn.ac.cags.util;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.springframework.util.ResourceUtils;



public class ImportExcelUtil {

    @SuppressWarnings("unchecked")
    public static List parseExcel(String sheetId, InputStream input) throws Exception {

        // 根据sheetId解析xml，获取Excel模板
        Element element = readXML(sheetId);
        String clazzString = element.attributeValue("class");

        // 从哪行开始解析
        int start = Integer.valueOf(element.attributeValue("startRow"));

        // 反射创建对象实例
        Class<? extends Object> clazz = Class.forName(clazzString);

        List<Element> columns = element.elements();

        Object instance = null;
        // 结果集
        List resultList = new ArrayList();
        // 要调用的方法
        Method method = null;
        // 调用Set方法要传递的参数
        Class<?>[] args = null;

        Cell cell = null;
        XSSFWorkbook wb = null;
        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

            // wb = new XSSFWorkbook(file);
            wb = new XSSFWorkbook(input);
            // 获取第一个Sheet页
            //XSSFSheet sheet = wb.getSheetAt(0);
            XSSFSheet sheet = wb.getSheet(sheetId);
            for (int i = start; i <= sheet.getLastRowNum(); i++) {
                Row row = sheet.getRow(i);
                if (row == null) {
                    continue;
                }
                instance = clazz.newInstance();

                StringBuffer buf = new StringBuffer();
                for (int j = 0; j < row.getLastCellNum(); j++) {
                    cell = row.getCell(j);
                    if (cell == null) {
                        continue;
                    }
                    args = new Class[1];
                    args[0] = getParameterType(columns.get(j).attributeValue("type"));
                    Object value;
                    try{
                        value = getCellValue(cell, args[0], dateFormat);
                        //累计字符串内容
                        buf.append(getStringValue(value));
                        //Date情况转成String,其他类型保持原样
                        args[0] = Date.class.equals(args[0]) ? String.class : args[0];

                        method = clazz.getDeclaredMethod("set" + columns.get(j).attributeValue("name"), args);
                        method.invoke(instance, value);
//                        if(null!=value){
//                            System.out.println(method+"被调用,值为:"+value);
//                        }
                    }catch (Exception e){
                        String errMsg=String.format("数据格式错误，行数：%d, 列数：%d  ,错误信息：%s",i+1,j+1,e.getMessage());
                        //throw new ImportException(errMsg);
                        System.out.println(errMsg);
                    }




                }

                //整行为空时丢弃该行数据
                if ("".equals(buf.toString().trim())) {
                    continue;
                }
                //加到集合中
                resultList.add(instance);
            }
        } catch (Exception e) {
            throw e;
        } finally {
            if (wb != null) {
                wb.close();
            }
        }
        return resultList;
    }

    public static boolean checkFileType(String filename) {
        if ((filename == null) || (filename.length() == 0)) {
            return false;
        }

        String type = "";
        int dot = filename.lastIndexOf('.');
        if ((dot > -1) && (dot < (filename.length() - 1))) {
            type = filename.substring(dot + 1);
        }
        if (!"xlsx".equalsIgnoreCase(type)) {
            return false;
        }
        return true;
    }

    @SuppressWarnings("unchecked")
    private static Element readXML(String sheetId) throws DocumentException, FileNotFoundException {
        File file = ResourceUtils.getFile("classpath:excel/sampleinfo.import.xml");
        SAXReader reader = new SAXReader();
        Document document = reader.read(file);
        Element root = document.getRootElement();
        Iterator<Element> iterator = root.elementIterator();
        Element element = null;
        while (iterator.hasNext()) {
            element = iterator.next();
            if (sheetId.equals(element.attributeValue("id"))) {
                break;
            }
        }
        return element;
    }

    private static Object getCellValue(Cell cell, Class<? extends Object> clazz, SimpleDateFormat dateFormat) {
        Object obj = null;
        switch (cell.getCellType()) {
            case BOOLEAN:
                obj = cell.getBooleanCellValue();
                break;
            case ERROR://CELL_TYPE_ERROR:
                obj = cell.getErrorCellValue();
                break;
            case NUMERIC://CELL_TYPE_NUMERIC:
                //用户自定义类型检测
                if (String.class.equals(clazz)) {
                    DecimalFormat df = new DecimalFormat("#.#########"); // 数字格式，防止长数字成为科学计数
                    obj = df.format(cell.getNumericCellValue());
                } else if (Date.class.equals(clazz)) {
                    obj = dateFormat.format(cell.getDateCellValue());
                } else if (Double.class.equals(clazz)) {
                    obj = cell.getNumericCellValue();
                } else if (Integer.class.equals(clazz)) {
                    DecimalFormat df = new DecimalFormat("#.#########"); // 数字格式，防止长数字成为科学计数
                    String val = df.format(cell.getNumericCellValue());
                    obj = Integer.parseInt(val);
                }
                break;
            case STRING://CELL_TYPE_STRING:
                String cellValue = cell.getStringCellValue();

                if (Double.class.equals(clazz)) {
                    Double d = Double.valueOf(cellValue);
                    obj = d;
                } else if (Integer.class.equals(clazz)) {
                    obj = Integer.parseInt(cellValue);
                } else {
                    obj = cellValue;
                }
                break;
            default:
                break;
        }

        return obj;
    }

    /**
     * 获取参数类型，默认为String
     *
     * @param parameterType
     * @return
     */
    private static Class<?> getParameterType(String parameterType) {
        switch (parameterType) {
            case "Byte":
                return Byte.class;
            case "Short":
                return Short.class;
            case "Integer":
                return Integer.class;
            case "Long":
                return Long.class;
            case "Float":
                return Float.class;
            case "Double":
                return Double.class;
            case "char":
                return char.class;
            case "String":
                return String.class;
            case "Date":
                return Date.class;
            default:
                return String.class;
        }
    }

    /**
     * 获取字符串内容
     *
     * @param obj
     * @return
     */
    private static String getStringValue(Object obj) {
        if (obj != null) {
            return String.valueOf(obj);
        }
        return "";
    }
}
