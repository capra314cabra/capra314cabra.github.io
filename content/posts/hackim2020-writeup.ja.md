---
title: "[CTF Writeup]HackIM 2020のWrite up"
date: 2020-02-09T17:54:45+09:00
draft: false
description: "HackIM 2020のWrite upです。解けている問題があまりにも少ないのは、気にしないで下さい..."
tags: ["CTF"]
---

Nullcon HackIM 2020に出たのでそのWrite upでも書こうかなーと思った次第です。

結論から申し上げますと、解けた問題は**1**問です...(しかも、その問題はコピペするだけ)

ただ、そんなのではWrite upとして意味をなさないので、競技終了後も作業していました。  
結局ZeldaAdventureの最初の1問を解くことができたのでそれをここに載せます。

### 問題の見た目

<img src="https://capra314cabra.github.io/imgs/hackim2020-game.jpg" alt="Game scene" class="center" width="500" height="300" />

Unity製のGameで、このNPC(白い敵)を1体以上倒すとFlagを手に入れられる、とあります。  
Playerは剣と体当たり(接触)することでNPCにダメージを与えられますが、敵のHPがとても高く、現実的な時間に倒せないようになっています。

### やったこと

UnityのWindowsでビルドした時のファイル構成は決まっています。  
特に、プログラマーが書いたコードは`AssemblyCSharp.dll`というファイルにコンパイルされて存在しています。

ここで、dnSpyを使用して`AssemblyCSharp.dll`の中のコードを読んでみます。  
コードの森を探索していると...

<img src="https://capra314cabra.github.io/imgs/hackim2020-code.jpg" alt="Decompiled code" class="center" width="483" height="129" />

ダメージを処理している部分を見つけました。  
HPが0になると`ShowSome`というコールチンを回し始めるようです。

<img src="https://capra314cabra.github.io/imgs/hackim2020-code.jpg" alt="Decompiled code" class="center" width="290" height="123" />

`ShowSome`をみると`this.textbox`を見せるようにしているみたいです。  
これはこのTextBoxがFlagを持っているのでしょう。  
dnSpyは実はDLLを編集する事が出来るので、この`this.textbox`を最初から表示させるようにコードを書き換えれば、Flagゲットです。

``` yaml
Flag: REVOLUTIONSTARTSWITHME
```

フォントがおしゃれすぎて読みにくかったです(褒めてます)

## おわりに

HackIM 2020の前に無力さを感じたので、もっと勉強してから出直します...

## 参考

[Unity-Game-Hacking](https://github.com/xcsh/Unity-game-hacking)
