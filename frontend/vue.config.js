const path = require('path');

module.exports = {
  //note: comment outputDir and assestsDir out if want to test npm run serve
  outputDir: path.resolve(__dirname,'../dist'),
  assetsDir: '../static',
  pages: {
    index: {
      // entry for the page
      entry: 'src/main.js',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'index.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Index Page',
    }
  }
};
