package com.publiccms.common.base;

import java.io.Serializable;
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletionStage;
import java.util.function.Function;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.search.highlight.Highlighter;
import org.apache.lucene.search.highlight.QueryScorer;
import org.apache.lucene.search.highlight.SimpleHTMLFormatter;
import org.hibernate.ObjectNotFoundException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;
import org.hibernate.search.backend.lucene.LuceneBackend;
import org.hibernate.search.engine.backend.Backend;
import org.hibernate.search.engine.search.predicate.dsl.SearchPredicateFactory;
import org.hibernate.search.engine.search.query.SearchResult;
import org.hibernate.search.engine.search.query.dsl.SearchQueryOptionsStep;
import org.hibernate.search.mapper.orm.Search;
import org.hibernate.search.mapper.orm.session.SearchSession;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.ReflectionUtils;
import org.springframework.web.util.HtmlUtils;

import com.publiccms.common.constants.Constants;
import com.publiccms.common.handler.FacetPageHandler;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;

/**
 * DAO基类
 * 
 * Base DAO
 * 
 * @param <E>
 * 
 */
public abstract class BaseDao<E> {
    protected final Log log = LogFactory.getLog(getClass());
    /**
     * 倒序
     * 
     * order type desc
     */
    public final static String ORDERTYPE_DESC = "desc";
    /**
     * 顺序
     * 
     * order type desc
     */
    public final static String ORDERTYPE_ASC = "asc";
    private Class<E> clazz;

    /**
     * 查询处理器
     * 
     * @param hql
     * @return queryhandler
     */
    public static QueryHandler getQueryHandler(String hql) {
        return new QueryHandler(hql);
    }

    /**
     * 查询处理器
     * 
     * @return queryhandler
     */
    public static QueryHandler getQueryHandler() {
        return new QueryHandler();
    }

    /**
     * Like查询
     * 
     * @param var
     * @return like query
     */
    public static String like(String var) {
        return "%" + var + "%";
    }

    /**
     * 右Like查询
     * 
     * @param var
     * @return right like query
     */
    public static String rightLike(String var) {
        return var + "%";
    }

    /**
     * 获取实体
     * 
     * @param id
     * @return entity
     */
    public E getEntity(Serializable id) {
        return null == id ? null : getSession().get(getEntityClass(), id);
    }

    /**
     * 获取实体
     * 
     * @param id
     * @param primaryKeyName
     * @return entity
     */
    public E getEntity(Serializable id, String primaryKeyName) {
        if (null == id) {
            return null;
        } else {
            QueryHandler queryHandler = getQueryHandler("from").append(getEntityClass().getSimpleName()).append("bean");
            queryHandler.condition("bean.").append(primaryKeyName).append("= :id").setParameter("id", id);
            return getEntity(queryHandler);
        }
    }

    /**
     * 获取实体集合
     * 
     * @param ids
     * @return entity list
     */
    public List<E> getEntitys(Serializable[] ids) {
        return getEntitys(ids, "id");
    }

    /**
     * 获取实体集合
     * 
     * @param ids
     * @param pk
     * @return entity list
     */
    public List<E> getEntitys(Serializable[] ids, String pk) {
        if (CommonUtils.notEmpty(ids)) {
            QueryHandler queryHandler = getQueryHandler("from").append(getEntityClass().getSimpleName()).append("bean");
            queryHandler.condition("bean.").append(pk).append("in (:ids)").setParameter("ids", ids);
            Query<E> query = getSession().createQuery(queryHandler.getSql(), getEntityClass());
            return getList(query, queryHandler);
        }
        return Collections.emptyList();
    }

    /**
     * 保存
     * 
     * @param entity
     * @return id
     */
    public Serializable save(E entity) {
        return getSession().save(init(entity));
    }

    /**
     * 删除
     * 
     * Delete
     * 
     * @param entity
     * 
     */
    public void delete(E entity) {
        if (null != entity) {
            getSession().delete(entity);
        }
    }

    /**
     * 删除
     * 
     * Delete
     * 
     * @param id
     */
    public void delete(Serializable id) {
        E entity = getEntity(id);
        if (null != entity) {
            getSession().delete(entity);
        }
    }

    /**
     * 获取实体
     * 
     * @param queryHandler
     * @return entity
     */
    protected E getEntity(QueryHandler queryHandler) {
        Query<E> query = getSession().createQuery(queryHandler.getSql(), getEntityClass());
        queryHandler.initQuery(query);
        try {
            return query.uniqueResult();
        } catch (Exception e) {
            return query.list().get(0);
        }
    }

    /**
     * 更新
     * 
     * @param queryHandler
     * @return number of data affected
     */
    protected int update(QueryHandler queryHandler) {
        Query<?> query = getSession().createQuery(queryHandler.getSql());
        queryHandler.initQuery(query);
        return query.executeUpdate();
    }

    /**
     * 刪除
     * 
     * @param queryHandler
     * @return number of data deleted
     */
    protected int delete(QueryHandler queryHandler) {
        return update(queryHandler);
    }

    /**
     * 获取列表
    * @param <T>
     * @param query
     * @param queryHandler
     * @return results list
     */
    protected <T> List<T> getList(Query<T> query, QueryHandler queryHandler) {
        queryHandler.initQuery(query);
        try {
            return query.list();
        } catch (ObjectNotFoundException e) {
            return query.setCacheable(false).list();
        }
    }

    /**
     * 获取列表
     * 
     * @param queryHandler
     * @return results list
     */
    protected List<E> getEntityList(QueryHandler queryHandler) {
        Query<E> query = getSession().createQuery(queryHandler.getSql(), getEntityClass());
        return getList(query, queryHandler);
    }

    /**
     * 获取列表
     * 
     * @param queryHandler
     * @return results list
     */
    protected List<?> getList(QueryHandler queryHandler) {
        Query<?> query = getSession().createQuery(queryHandler.getSql());
        return getList(query, queryHandler);
    }

    /**
     * @param queryHandler
     * @param pageIndex
     * @param pageSize
     * @param maxResults
     * @return results page
     */
    protected PageHandler getPage(QueryHandler queryHandler, Integer pageIndex, Integer pageSize, Integer maxResults) {
        return getPage(queryHandler, null, pageIndex, pageSize, maxResults);
    }

    /**
     * @param queryHandler
     * @param pageIndex
     * @param pageSize
     * @return page
     */
    protected PageHandler getPage(QueryHandler queryHandler, Integer pageIndex, Integer pageSize) {
        return getPage(queryHandler, pageIndex, pageSize, Integer.MAX_VALUE);
    }

    /**
     * @param queryHandler
     * @param countHql
     * @param pageIndex
     * @param pageSize
     * @param maxResults
     * @return results page
     */
    protected PageHandler getPage(QueryHandler queryHandler, String countHql, Integer pageIndex, Integer pageSize,
            Integer maxResults) {
        PageHandler page = new PageHandler(pageIndex, pageSize);
        if (null == pageSize) {
            queryHandler.setMaxResults(maxResults);
            List<?> list = getList(queryHandler);
            page.setList(list);
            page.setTotalCount(list.size());
        } else {
            page.setTotalCount(countResult(queryHandler, countHql));
            if (0 != pageSize) {
                queryHandler.setFirstResult(page.getFirstResult()).setMaxResults(page.getPageSize());
                page.setList(getList(queryHandler));
            }
            if (null != maxResults && page.getTotalCount() > maxResults) {
                page.setTotalCount(maxResults);
            }
        }
        return page;
    }

    /**
     * @param optionsStep
     * @param highLighterQuery
     * @param pageIndex
     * @param pageSize
     * @return page
     */
    protected PageHandler getPage(SearchQueryOptionsStep<?, E, ?, ?, ?> optionsStep, HighLighterQuery highLighterQuery,
            Integer pageIndex, Integer pageSize) {
        return getPage(optionsStep, highLighterQuery, pageIndex, pageSize, Integer.MAX_VALUE);
    }

    /**
     * @param optionsStep
     * @param highLighterQuery
     * @param pageIndex
     * @param pageSize
     * @param maxResults
     * @return results page
     */
    protected PageHandler getPage(SearchQueryOptionsStep<?, E, ?, ?, ?> optionsStep, HighLighterQuery highLighterQuery,
            Integer pageIndex, Integer pageSize, Integer maxResults) {
        PageHandler page = new PageHandler(pageIndex, pageSize);
        SearchResult<E> result;
        if (null == pageSize) {
            result = optionsStep.fetch(0, maxResults);
            page.setTotalCount(result.total().hitCount());
        } else {
            if (0 == pageSize) {
                result = optionsStep.fetch(0, 1);
            } else {
                result = optionsStep.fetch(page.getFirstResult(), page.getPageSize());
            }

            page.setTotalCount(result.total().hitCount());
            if (null != maxResults && page.getTotalCount() > maxResults) {
                page.setTotalCount(maxResults);
            }
        }

        List<E> resultList = result.hits();
        higtLighter(resultList, highLighterQuery);
        page.setList(resultList);
        return page;
    }

    /**
     * @param optionsStep
     * @param facetFieldKeys
     * @param facetFieldResult
     * @param highLighterQuery
     * @param pageIndex
     * @param pageSize
     * @return page
     */
    protected FacetPageHandler getFacetPage(SearchQueryOptionsStep<?, E, ?, ?, ?> optionsStep,
            Function<SearchQueryOptionsStep<?, E, ?, ?, ?>, SearchQueryOptionsStep<?, E, ?, ?, ?>> facetFieldKeys,
            Function<SearchResult<E>, Map<String, Map<String, Long>>> facetFieldResult, HighLighterQuery highLighterQuery,
            Integer pageIndex, Integer pageSize) {
        return getFacetPage(optionsStep, facetFieldKeys, facetFieldResult, highLighterQuery, pageIndex, pageSize,
                Integer.MAX_VALUE);
    }

    /**
     * @param optionsStep
     * @param facetFieldKeys
     * @param facetFieldResult
     * @param highLighterQuery
     * @param pageIndex
     * @param pageSize
     * @param maxResults
     * @return results page
     */
    protected FacetPageHandler getFacetPage(SearchQueryOptionsStep<?, E, ?, ?, ?> optionsStep,
            Function<SearchQueryOptionsStep<?, E, ?, ?, ?>, SearchQueryOptionsStep<?, E, ?, ?, ?>> facetFieldKeys,
            Function<SearchResult<E>, Map<String, Map<String, Long>>> facetFieldResult, HighLighterQuery highLighterQuery,
            Integer pageIndex, Integer pageSize, Integer maxResults) {
        FacetPageHandler page = new FacetPageHandler(pageIndex, pageSize);
        facetFieldKeys.apply(optionsStep);
        SearchResult<E> result;
        if (null == pageSize) {
            result = optionsStep.fetch(0, maxResults);
            page.setTotalCount(result.total().hitCount());
        } else {
            if (0 == pageSize) {
                result = optionsStep.fetch(0, 1);
            } else {
                result = optionsStep.fetch(page.getFirstResult(), page.getPageSize());
            }
            page.setTotalCount(result.total().hitCount());
            if (null != maxResults && page.getTotalCount() > maxResults) {
                page.setTotalCount(maxResults);
            }
        }
        List<E> resultList = result.hits();
        higtLighter(resultList, highLighterQuery);
        page.setList(resultList);
        page.setFacetMap(facetFieldResult.apply(result));
        return page;
    }

    /**
     * @param resultList
     * @param highLighterQuery
     */
    protected void higtLighter(List<E> resultList, HighLighterQuery highLighterQuery) {
        if (highLighterQuery.isHighlight() && null != highLighterQuery.getQuery()
                && CommonUtils.notEmpty(highLighterQuery.getFields())) {
            SimpleHTMLFormatter formatter;
            if (CommonUtils.notEmpty(highLighterQuery.getPreTag()) && CommonUtils.notEmpty(highLighterQuery.getPostTag())) {
                formatter = new SimpleHTMLFormatter(highLighterQuery.getPreTag(), highLighterQuery.getPostTag());
            } else {
                formatter = new SimpleHTMLFormatter();
            }
            Backend backend = getSearchBackend();
            Analyzer analyzer;
            if (backend instanceof LuceneBackend) {
                analyzer = backend.unwrap(LuceneBackend.class).analyzer("cms").get();
            } else {
                analyzer = new StandardAnalyzer();
            }
            QueryScorer queryScorer = new QueryScorer(highLighterQuery.getQuery(), highLighterQuery.getDefaultFieldName());
            Highlighter highlighter = new Highlighter(formatter, queryScorer);
            for (E e : resultList) {
                for (String fieldName : highLighterQuery.getFields()) {
                    try {
                        Method method = BeanUtils.getPropertyDescriptor(getEntityClass(), fieldName).getReadMethod();
                        if (null != method) {
                            Object fieldValue = ReflectionUtils.invokeMethod(method, e);
                            String hightLightFieldValue = null;
                            if (fieldValue instanceof String && CommonUtils.notEmpty(String.valueOf(fieldValue))) {
                                String safeValue = HtmlUtils.htmlEscape(String.valueOf(fieldValue),
                                        Constants.DEFAULT_CHARSET_NAME);
                                hightLightFieldValue = highlighter.getBestFragment(analyzer, fieldName, safeValue);
                                if (CommonUtils.notEmpty(hightLightFieldValue)) {
                                    ReflectionUtils.invokeMethod(
                                            BeanUtils.getPropertyDescriptor(getEntityClass(), fieldName).getWriteMethod(), e,
                                            hightLightFieldValue);
                                } else {
                                    ReflectionUtils.invokeMethod(
                                            BeanUtils.getPropertyDescriptor(getEntityClass(), fieldName).getWriteMethod(), e,
                                            safeValue);
                                }
                            }
                        }
                    } catch (Exception ignore) {
                        ignore.printStackTrace();
                    }
                }
            }
        }
    }

    /**
     * @param queryHandler
     * @param countHql
     * @return number of results
     */
    protected long countResult(QueryHandler queryHandler, String countHql) {
        if (CommonUtils.empty(countHql)) {
            countHql = queryHandler.getCountSql();
        }
        Query<?> query = getSession().createQuery(countHql);
        List<?> list = queryHandler.initQuery(query, false).list();
        if (list.isEmpty()) {
            return 0;
        } else {
            Number result = (Number) list.iterator().next();
            if (null == result) {
                return 0;
            } else {
                return result.longValue();
            }
        }
    }

    /**
     * @param queryHandler
     * @return number of data
     */
    protected long count(QueryHandler queryHandler) {
        Query<?> query = getSession().createQuery(queryHandler.getSql());
        List<?> list = queryHandler.initQuery(query, false).list();
        if (list.isEmpty()) {
            return 0;
        } else {
            Number result = (Number) list.iterator().next();
            if (null == result) {
                return 0;
            } else {
                return result.longValue();
            }
        }
    }

    /**
     * @param entity
     */
    protected void index(E entity) {
        getSearchSession().indexingPlan().addOrUpdate(entity);
    }

    /**
     * @return CompletionStage
     */
    public CompletionStage<?> reCreateIndex() {
        SearchSession searchSearch = getSearchSession();
        return searchSearch.massIndexer().start();
    }

    /**
     * @return SearchPredicateFactory
     */
    protected SearchPredicateFactory getSearchPredicateFactory() {
        return getSearchSession().scope(getEntityClass()).predicate();
    }

    /**
     * @return session
     */
    protected Session getSession() {
        return sessionFactory.getCurrentSession();
    }

    /**
     * @return fulltext session
     */
    protected SearchSession getSearchSession() {
        return Search.session(sessionFactory.getCurrentSession());
    }

    /**
     * @return backend
     */
    public Backend getSearchBackend() {
        return Search.mapping(sessionFactory).backend();
    }

    @SuppressWarnings("unchecked")
    protected Class<E> getEntityClass() {
        return null == clazz
                ? this.clazz = (Class<E>) ((ParameterizedType) getClass().getGenericSuperclass()).getActualTypeArguments()[0]
                : clazz;
    }

    protected abstract E init(E entity);

    @Autowired
    protected SessionFactory sessionFactory;
}
