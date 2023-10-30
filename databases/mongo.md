# Mongo

### Mongo service
```bash
sudo service mongod status
sudo service mongod restart
```


### Mongo Shell
```bash
show dbs
use <database>
show collections
```
```js
// Select data from collection
db.collectionName.find().pretty()

// To fetch files_id only from fs.chunks collection
db.fs.chunks.find({}, {files_id: 1}).pretty()

// fetch import_path from fs.files collection and supress _id
db.fs.files.find({}, {_id:0, import_path: 1})

// Count
db.modulestore.structures.find({}).count()

//To see the function sourse code (enter without braces)
db.modulestore.structures.find

// select docs ids where schema_version == 1
db.modulestore.structures.find({schema_version: {$eq: 1}}, {_id:1})

// set index on main_ingredient field
db.recipies.ensureIndex({
    main_ingredient: 1
})

// or compound index on two fields:
db.recipies.ensureIndex({
    main_ingredient: 1,
    calories: -1 // in descending order
})

// get collection indexes
db.recipies.getIndexes()
db.recipies.getIndexKeys()

// Drop specific index
db.recipies.dropIndex({ ingredients: 1 })

// drop all indexes and recreate them
db.recipies.reIndex()
```




#### Connect to mongodb:
```shell
export LC_ALL=C
mongo -u <user> -p <password> <database>
mongo -u edxapp -p hRWM8qmzSIN1iFxTW93EppoK5gi3KPLQbaB edxapp
```
