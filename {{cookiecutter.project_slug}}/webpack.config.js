'use strict'

// noinspection JSUnresolvedFunction
// eslint-disable-next-line @typescript-eslint/no-var-requires,no-undef
const path = require('path')

// noinspection JSUnresolvedVariable,JSUnresolvedFunction
// eslint-disable-next-line no-undef
module.exports = {
    entry: {
        '{{ cookiecutter.project_slug }}': ['./{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.js', './{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.scss']
    }, resolve: {
        extensions: ['.ts', '.js', '.json']
    }, output: {
        // eslint-disable-next-line no-undef
        path: path.resolve(__dirname, '.'), filename: './{{ cookiecutter.project_slug }}/static/js/[name].js'
    }, optimization: {
        minimize: false
    },

    module: {
        rules: [{
            test: /\.tsx?$/, use: 'ts-loader', exclude: /node_modules/
        }, {
            test: /\.scss$/, exclude: /node_modules/, use: [{
                loader: 'file-loader',
                options: {outputPath: '.', name: './{{ cookiecutter.project_slug }}/static/css/[name].min.css'}
            }, 'sass-loader']
        }]
    }, // Useful for debugging.
    devtool: 'source-map', performance: {hints: false}
}
