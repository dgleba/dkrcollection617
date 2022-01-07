const webpack = require('webpack')
const merge = require('webpack-merge')

// const webpackBaseConfig = require('./webpack.config.base.js')

const webpackConfig = merge(webpackBaseConfig, {
  mode: process.env.NODE_ENV,
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    disableHostCheck: true
  },

})

module.exports = webpackConfig

