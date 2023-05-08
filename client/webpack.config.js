const path = require('path');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const prod = process.env.NODE_ENV === 'production';
const {NODE_ENV = 'production'} = process.env;

module.exports = {
  mode: NODE_ENV,
  entry: './src/index.tsx',
  watch: NODE_ENV === 'development',
  output: {
    path: path.resolve(__dirname, '..', 'task_service', 'static', 'dist')
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        exclude: /node_modules/,
        resolve: {
          extensions: ['.ts', '.tsx', '.js', '.json'],
        },
        use: 'ts-loader',
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
    ]
  },
  devtool: NODE_ENV == 'development' ? 'source-map': undefined,
  plugins: [
    new MiniCssExtractPlugin(),
  ],
};