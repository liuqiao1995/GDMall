//app.js
import {Login} from './utils/login.js'

var login = new Login();


App({
    onLaunch: function () {
        // 展示本地存储能力
        var logs = wx.getStorageSync('logs') || []
        logs.unshift(Date.now())
        wx.setStorageSync('logs', logs)

        // 判断是否登录
        // wx.checkSession({
        //     success: function (res) {
        //         console.log(res, '登录未过期')
                // wx.showToast({
                //     title: '登录未过期啊',
                // })
            // },
            // fail: function (res) {
            //     console.log(res, '登录过期了')
                // wx.showModal({
                //     title: '提示',
                //     content: '你的登录信息过期了，请重新登录',
                // })
                // 登录
                wx.login({
                    success: res => {
                        // 获取用户token
                        var token = login.getToken();
                        if (token.length == 64) {
                            // 存在token,查询redis是否存在该token
                            login.findToken((res) => {
                                if (res.msg == 'success') {
                                    console.log('登录成功！')
                                } else {
                                    // 获取用户code，返回token
                                    login.findWxUser(res.code, (res) => {
                                        console.log(res)
                                        // 保存到缓存
                                        wx.setStorageSync('token', res.token)
                                    })
                                }
                            })
                        } else {
                            // 不存在token
                            // 获取用户code，返回token
                            login.findWxUser(res.code, (res) => {
                                console.log(res)
                                // 保存到缓存
                                wx.setStorageSync('token', res.token)
                            })
                        }


                    }
                })
        //     }
        // });


        // 获取用户信息
        wx.getSetting({
            success: res => {
                if (res.authSetting['scope.userInfo']) {
                    // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
                    wx.getUserInfo({
                        success: res => {
                            // 可以将 res 发送给后台解码出 unionId
                            this.globalData.userInfo = res.userInfo

                            // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
                            // 所以此处加入 callback 以防止这种情况
                            if (this.userInfoReadyCallback) {
                                this.userInfoReadyCallback(res)
                            }
                        }
                    })
                }
            }
        })
    },
    globalData: {
        userInfo: null,
        is_query: 0
    }


})