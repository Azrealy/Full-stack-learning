const Sequelize = require('sequelize');
const sequelize = new Sequelize('database', 'username', 'password', {
    // sqlite! now!
    dialect: 'sqlite',
  
    // the storage engine for sqlite
    // - default ':memory:'
    storage: '/tmp/database.sqlite'
  })
sequelize.authenticate().then(()=> {
    console.log('connection to postgre sucess')  
}).catch(err=> {
    console.error('Unable to connect to the database:', err)
})