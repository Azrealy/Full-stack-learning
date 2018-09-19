import Sequelize from 'sequelize';

const sequelize = new Sequelize('database', 'username', 'password', {
    // sqlite! now!
    dialect: 'sqlite',
  
    // the storage engine for sqlite
    // - default ':memory:'
    storage: '/tmp/database.sqlite'
  })

const models = {
    User: sequelize.import('./user'),
    Message: sequelize.import('./message'),
  };

Object.keys(models).forEach(key => {
    if ('associate' in models[key]) {
      models[key].associate(models);
    }
  });
export { sequelize };

export default models;