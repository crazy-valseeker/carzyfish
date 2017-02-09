/**
 * Created by valseek on 17-2-5.
 */

var path = require('path');
var client_dir="dist/javascript";
var server_dir="../web_server/static/javascript"

module.exports = {
    entry: {
        index:'./dev/apps/index.js'
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, server_dir)
    },
    module: {
        rules: [
            {
                test: /\.less$/,
                use: [
                    'style-loader',
                    { loader: 'css-loader', options: { importLoaders: 1 } },
                    'less-loader'
                ]
            },
            {
                test:/\.js/,
                use:[
                    {
                        loader:'babel-loader',
                        options:{
                            presets: ['react','es2015']
                        }
                    }
                ],
            }
        ]
    },
    externals: {
        "react": 'React',
        'react-dom': 'ReactDOM'
    }
};