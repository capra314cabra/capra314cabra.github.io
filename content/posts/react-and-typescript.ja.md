---
title: "Reactと一緒にTypescriptをどうぞ"
date: 2019-12-09T21:52:06+09:00
description: "ReactでWebアプリケーションを作るときはTypescriptを利用してメンテナンス性を高めた方が良いのでは、という話です。"
draft: false
author: capra314cabra
tags: ["Typescript", "React"]
keyword: "Typescript,React,Webpack"
---

ReactでWebアプリを作ったのですがその時にTypescriptを導入したらその前より作業が捗りました。信じるか信じないかはあなた次第ですが。  
そのようなこともあったので、この記事ではReactによる開発にTypescriptを導入する方法をお伝えします。

## 作ったもの

クイズを作成し挑戦出来るサイト。[Bluespoon](https://capra314cabra.github.io/blue-spoon/index.html) [コード](https://github.com/capra314cabra/blue-spoon)

<img src="https://capra314cabra.github.io/blue-spoon/img/logo.svg" alt="Bluespoon Logo" class="center" width="200" height="200" />

宣伝です。はい。

## 必要な環境

Node jsをインストールしている前提です。  
手元の環境はこんな感じです。

``` bash
node --version
# Output: v12.10.0
```

EditorはVisual Studio Codeを使っています。使用を強くお勧めします。Typescriptとの親和性が高いです。  
Microsoft製品を避けたい人もVisual Studio Codeだけでいいので許してあげてください。

## パッケージのインストール

コマンドを打っていきましょう。

``` bash
mkdir app-dir
cd app-dir
```

プロジェクトのディレクトリが出来たと思います。  
続いて必要なアイテムをインストールします。まずはreactのパッケージから。

``` bash
npm install -S react react-dom
```

次は開発にのみ必要なアイテムをインストールします。

``` bash
# Typescript関係
npm install -D typescript source-map-loader ts-loader ts-node
# Webpack関係
npm install webpack webpack-cli
# 型定義ファイル
npm install -D @types/node @types/react @types/react-dom @types/webpack
```

沢山インストールしましたね。それぞれ解説していきます。ここは読み飛ばして大丈夫です。

| モジュール | 説明 |
|:---------|:---------|
| react react-dom | React本体です |
| typescript | Typescriptを使う時に必要です。 |
| source-map-loader ts-loader | Webpackでビルドする時にファイルの探索やコードのマップを作ってくれます。 |
| ts-node | TypescriptをJavaScriptのように実行できるようになります。Webpackのwebpack.config.jsをTypescriptで書くとなると必要です。 |
| webpack webpack-cli | JavaScriptをトランスパイルします。詳しくはググってください。説明しきれません。 |
| @types/* | Typescriptでモジュールを使うときにとても便利です。なかったらTypescriptを使う意味が半減します。 |

こんな感じですね。

## Webpackでビルド出来るようにする

Webpackはインストールしただけでは何も起こりません。
Webpackに何をするか"指示する"ファイルが必要となります。  
そのファイルは"webpack.config.js"と名前を付ける事になっていますが、これって...

そう!JavaScriptのファイルです!

折角なのでこれをTypesciptで書きましょう。ファイル名は"webpack.config.ts"にします。
JavaScriptでしかWebpackを使ったことがない人はきっと感涙することでしょう。~~(大袈裟)~~

``` typescript
// webpack.config.ts

import * as webpack from "webpack";
import * as path from "path";

// どの種類のファイルをどのように処理するか
const rules: webpack.Rule[] = [
    {
        test: /\.ts(x?)$/,
        exclude: /node_modules/,
        use: [
            {
                loader: "ts-loader"
            }
        ]
    },
    {
        enforce: "pre",
        test: /\.js$/,
        loader: "source-map-loader"
    }
];

const webpackModule: webpack.Module = {
    rules: rules
};

const config: webpack.Configuration = {
    mode: "production",

    devtool: "source-map",

    entry: {
        // 開始するスクリプトを指定する
        index: "./src/index.tsx"
    },

    resolve: {
        // importの時に以下の拡張子であれば省略ができる
        extensions: [".ts", ".tsx", ".js", ".jsx"]
    },

    output: {
        // /dist に出力する
        filename: "[name].bundle.js",
        path: path.resolve(process.cwd() + "/dist")
    },

    module: webpackModule,

    // Reactは外部参照とする (そうしないと出力されたファイルのサイズが大きい)
    // 勿論、<script>タグなどの使用が前提
    externals: {
        "react": "React",
        "react-dom": "ReactDOM",
    }
};

export default config;
```

JavaScriptで書くよりも長くなっていますね。
ただ、このパラメータをいじるときに推論が効きますし、型を間違えるとエラーか警告を出してくれます。  
メンテナンス性が上がります。

これらが終わればあとは

``` bash
npx webpack
```

で実行できます。

おめでとうございます！これであなたもTypescriptでReactを使用した開発ができます!
