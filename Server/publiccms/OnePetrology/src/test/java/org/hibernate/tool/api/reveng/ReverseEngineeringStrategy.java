package org.hibernate.tool.api.reveng;

import java.util.List;
import java.util.Map;
import java.util.Properties;

import org.hibernate.mapping.Column;
import org.hibernate.mapping.ForeignKey;
import org.hibernate.mapping.MetaAttribute;
import org.hibernate.mapping.Table;
import org.hibernate.tool.api.dialect.MetaDataDialect;

public interface ReverseEngineeringStrategy {

    /**
     * Generic method used to initialize the reverse engineering strategy.
     * 
     * @param settings
     *            used for this
     */
    void setSettings(ReverseEngineeringSettings settings);

    /**
     * Configure the reverse engineering strategy. Called before reverse
     * engineering commences.
     * 
     * This is mainly for exotic strategies to get access to a connection.
     * 
     * @param runtimeInfo
     */
    void configure(ReverseEngineeringRuntimeInfo runtimeInfo);

    /**
     * Close any resources this strategy might have used. Called after reverse
     * engineering has been completed.
     */
    void close();

    /**
     * 
     * @param tableIdentifier
     * @return a fully-qualified class name
     */
    String tableToClassName(TableIdentifier tableIdentifier);

    /**
     * Return a property name for a Column.
     * 
     * @param table
     * @param column
     *            a columnname
     * @return a property name
     */
    String columnToPropertyName(TableIdentifier table, String column);

    boolean excludeTable(TableIdentifier ti);

    boolean excludeColumn(TableIdentifier identifier, String columnName);

    /**
     * Gets the preferred Hibernate type for an SQL type.
     * 
     * @param table
     *            name of the table, can be null
     * @param columnName
     *            name of the column, can be null
     * @param sqlType
     *            The sql type.
     * @param length
     *            The length of the column.
     * @param precision
     *            The number of decimal digits, if applicable.
     * @param scale
     *            The scale, if applicable.
     * @param nullable
     *            The nullability of the column
     * @param generatedIdentifier
     *            true if for a column used in an identifier that is not
     *            "assigned", false otherwise.
     * @return The Preferred hibernate type name.
     */
    String columnToHibernateTypeName(TableIdentifier table, String columnName, int sqlType, int length, int precision,
                                     int scale, boolean nullable, boolean generatedIdentifier);

    /**
     * Gets the user defined foreign keys.
     * 
     * @param referencedTable
     *            the table to get the foreign keys for
     * @return a list of ForeignKey's
     */
    List<ForeignKey> getForeignKeys(TableIdentifier referencedTable);

    /**
     * @param identifier
     *            the table to look up for
     * @return the identifier strategy name wanted for a specific table, null if
     *         use what the database metadata can tell.
     */
    String getTableIdentifierStrategyName(TableIdentifier identifier);

    Properties getTableIdentifierProperties(TableIdentifier identifier);

    /**
     * If a table does not have any primarykey columns reported, this method is
     * called.
     * 
     * @param identifier
     * @return list of strings for each column name that is part of the primary
     *         key
     **/
    List<String> getPrimaryKeyColumnNames(TableIdentifier identifier);

    /**
     * Given a class name return the name for its composite id if it will have
     * one.
     * 
     * @param className
     * @return
     */
    String classNameToCompositeIdName(String className);

    /**
     * Return explicit which column name should be used for optimistic lock
     * 
     * @param identifier
     * @return
     */
    String getOptimisticLockColumnName(TableIdentifier identifier);

    boolean useColumnForOptimisticLock(TableIdentifier identifier, String column);

    /**
     * Return list of SchemaSelctors to be used when asking
     * {@link MetaDataDialect} for metadata.
     * 
     * @return list of {@link SchemaSelection} instances
     */
    List<SchemaSelection> getSchemaSelections();

    /**
     * Given a table name, return the wanted name for the identifier.
     * 
     * @param tableIdentifier
     * @return name to be used for identification
     */
    String tableToIdentifierPropertyName(TableIdentifier tableIdentifier);

    /**
     * Given a table name, return the wanted name for a composite identifier.
     * 
     * @param identifier
     * @return
     */
    String tableToCompositeIdName(TableIdentifier identifier);

    /**
     * Return the list of metaattributes to assign to classes created based on
     * the given table
     * 
     * @param tableIdentifier
     * @return a Map from String to {@link MetaAttribute}
     */
    Map<String, MetaAttribute> tableToMetaAttributes(TableIdentifier tableIdentifier);

    /**
     * Return the list of metaattributes to assign to properties created based
     * on the given column
     * 
     * @param identifier
     * @param column
     * @return a Map from String to {@link MetaAttribute}
     */
    Map<String, MetaAttribute> columnToMetaAttributes(TableIdentifier identifier, String column);

    /**
     * Should this foreignkey be excluded as a oneToMany
     * 
     * @param keyname
     * @param fromTable
     * @param fromColumns
     * @param referencedTable
     * @param referencedColumns
     * @return
     */
    boolean excludeForeignKeyAsCollection(String keyname, TableIdentifier fromTable, List<Column> fromColumns,
                                          TableIdentifier referencedTable, List<Column> referencedColumns);

    /**
     * Should this foreignkey be excluded as a many-to-one
     * 
     * @param keyname
     * @param fromTable
     * @param fromColumns
     * @param referencedTable
     * @param referencedColumns
     * @return
     */
    boolean excludeForeignKeyAsManytoOne(String keyname, TableIdentifier fromTable, List<?> fromColumns,
                                         TableIdentifier referencedTable, List<?> referencedColumns);

    /**
     * is the collection inverse or not ?
     * 
     * @param name
     * @param foreignKeyTable
     * @param columns
     * @param foreignKeyReferencedTable
     * @param referencedColumns
     * @return
     */
    boolean isForeignKeyCollectionInverse(String name, TableIdentifier foreignKeyTable, List<?> columns,
                                          TableIdentifier foreignKeyReferencedTable, List<?> referencedColumns);

    /**
     * is the collection lazy or not ?
     * 
     * @param name
     * @param foreignKeyTable
     * @param columns
     * @param foreignKeyReferencedTable
     * @param referencedColumns
     * @return
     */
    boolean isForeignKeyCollectionLazy(String name, TableIdentifier foreignKeyTable, List<?> columns,
                                       TableIdentifier foreignKeyReferencedTable, List<?> referencedColumns);

    /**
     * Return a collection role name for a Collection based on the foreignkey.
     * 
     * @param keyname
     * @param fromTable
     * @param fromColumns
     *            list of Column instances on the fromTable. Only col.getName()
     *            should be assumed to be correct
     * @param referencedTable
     * @param referencedColumns
     *            list of Column instances on the referenced Table. Only
     *            col.getName() should be assumed to be correct
     * @param uniqueReference
     *            true if there is no other references to the same table
     * @return
     */
    String foreignKeyToCollectionName(String keyname, TableIdentifier fromTable, List<?> fromColumns,
                                      TableIdentifier referencedTable, List<?> referencedColumns, boolean uniqueReference);

    /**
     * 
     * @param keyname
     * @param fromTable
     * @param fromColumns
     *            list of Column instances on the fromTable. Only col.getName()
     *            should be assumed to be correct
     * @param referencedTable
     * @param referencedColumns
     *            list of Column instances on the referenced Table. Only
     *            col.getName() should be assumed to be correct
     * @param uniqueReference
     *            true if there is no other references to the same table
     * @return
     */
    String foreignKeyToEntityName(String keyname, TableIdentifier fromTable, List<?> fromColumns,
                                  TableIdentifier referencedTable, List<?> referencedColumns, boolean uniqueReference);

    /**
     * Used to rename the inverse one-to-one properties.
     * 
     * @param keyname
     * @param fromTable
     * 
     * @param fromColumns
     *            list of Column instances on the fromTable. Only col.getName()
     *            should be assumed to be correct
     * @param referencedTable
     * @param referencedColumns
     *            list of Column instances on the referenced Table. Only
     *            col.getName() should be assumed to be correct
     * @param uniqueReference
     *            true if there is no other references to the same table
     * @return null if use defaults or non-empty String with a specific name
     */
    String foreignKeyToInverseEntityName(String keyname, TableIdentifier fromTable, List<?> fromColumns,
                                         TableIdentifier referencedTable, List<?> referencedColumns, boolean uniqueReference);

    /**
     * @param table
     * @return true if this table is considered to be a many-to-many table.
     */
    boolean isManyToManyTable(Table table);

    /**
     * 
     * @param fromKey
     *            list of Column instances on the fromTable. Only col.getName()
     *            should be assumed to be correct
     * @param middleTable
     * @param toKey
     * @param uniqueReference
     *            true if there is no other references to the same table
     * @return
     */
    String foreignKeyToManyToManyName(ForeignKey fromKey, TableIdentifier middleTable, ForeignKey toKey,
                                      boolean uniqueReference);

    boolean isOneToOne(ForeignKey foreignKey);

    AssociationInfo foreignKeyToAssociationInfo(ForeignKey foreignKey);

    AssociationInfo foreignKeyToInverseAssociationInfo(ForeignKey foreignKey);

}
