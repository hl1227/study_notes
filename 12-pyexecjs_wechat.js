!function(c) {
    function e(e) {
        for (var t, n, o = e[0], r = e[1], i = e[2], s = 0, a = []; s < o.length; s++)
            n = o[s],
            Object.prototype.hasOwnProperty.call(d, n) && d[n] && a.push(d[n][0]),
            d[n] = 0;
        for (t in r)
            Object.prototype.hasOwnProperty.call(r, t) && (c[t] = r[t]);
        for (l && l(e); a.length; )
            a.shift()();
        return p.push.apply(p, i || []),
        u()
    }
    function u() {
        for (var e, t = 0; t < p.length; t++) {
            for (var n = p[t], o = !0, r = 1; r < n.length; r++) {
                var i = n[r];
                0 !== d[i] && (o = !1)
            }
            o && (p.splice(t--, 1),
            e = s(s.s = n[0]))
        }
        return e
    }
    var n = {}
      , d = {
        "login/loginpage/loginpage": 0
    }
      , p = [];
    function s(e) {
        if (n[e])
            return n[e].exports;
        var t = n[e] = {
            i: e,
            l: !1,
            exports: {}
        };
        return c[e].call(t.exports, t, t.exports, s),
        t.l = !0,
        t.exports
    }
    s.m = c,
    s.c = n,
    s.d = function(e, t, n) {
        s.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: n
        })
    }
    ,
    s.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    s.t = function(t, e) {
        if (1 & e && (t = s(t)),
        8 & e)
            return t;
        if (4 & e && "object" == typeof t && t && t.__esModule)
            return t;
        var n = Object.create(null);
        if (s.r(n),
        Object.defineProperty(n, "default", {
            enumerable: !0,
            value: t
        }),
        2 & e && "string" != typeof t)
            for (var o in t)
                s.d(n, o, function(e) {
                    return t[e]
                }
                .bind(null, o));
        return n
    }
    ,
    s.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return s.d(t, "a", t),
        t
    }
    ,
    s.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    s.p = "/mpres/zh_CN/htmledition/";
    var r = (t = window.webpackJsonp = window.webpackJsonp || []).push.bind(t);
    t.push = e;
    for (var t = t.slice(), o = 0; o < t.length; o++)
        e(t[o]);
    var l = r;
    p.push([34, "pages/modules~advanced/menusetting4Web1~album/edit/edit~album/list/list~biztransfer/index/index~brandcompl~modules", "pages/vendors~advanced/menusetting4Web1~album/edit/edit~album/list/list~biztransfer/index/index~brandcompl~vendors", "pages/modules~advanced/menusetting4Web1~album/edit/edit~city/service_edit/service_edit~complain/public_com~modules", "pages/threerd~advanced/menusetting4Web1~album/edit/edit~city/service_edit/service_edit~complain/public_com~threerd"]),
    u()
}({
    "./src/3rd/cookie/cookie.js": function(e, t, n) {
        n = function(e, t, n) {
            var o = /\+/g;
            function l(e) {
                return e
            }
            function m(e) {
                var t;
                try {
                    t = function(e) {
                        0 === e.indexOf('"') && (e = e.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, "\\"));
                        return e
                    }(decodeURIComponent(e.replace(o, " ")))
                } catch (e) {
                    t = ""
                }
                return t
            }
            function f(e) {
                return g.json ? JSON.parse(e) : e
            }
            var r = {}
              , g = r.cookie = function(e, t, n) {
                var o, r;
                if (void 0 !== t)
                    return n = function(e) {
                        for (var t = 1, n = arguments.length; t < n; t++)
                            for (var o in arguments[t])
                                e[o] = arguments[t][o];
                        return e
                    }({}, g.defaults, n),
                    null === t && (n.expires = -1),
                    "number" == typeof n.expires && (o = n.expires,
                    (r = n.expires = new Date).setDate(r.getDate() + o)),
                    t = g.json ? JSON.stringify(t) : String(t),
                    document.cookie = [encodeURIComponent(e), "=", g.raw ? t : encodeURIComponent(t), n.expires ? "; expires=" + n.expires.toUTCString() : "", n.path ? "; path=" + n.path : "", n.domain ? "; domain=" + n.domain : "", n.secure ? "; secure" : ""].join("");
                for (var i = g.raw ? l : m, s = document.cookie.split("; "), a = e ? null : {}, c = 0, d = s.length; c < d; c++) {
                    var u = s[c].split("=")
                      , p = i(u.shift())
                      , u = i(u.join("="));
                    if (e && e === p) {
                        a = f(u);
                        break
                    }
                    e || (a[p] = f(u))
                }
                return a
            }
            ;
            g.defaults = {},
            r.remove = function(e, t) {
                return null !== this.cookie(e) && (this.cookie(e, null, t),
                !0)
            }
            ,
            n.exports = r
        }
        .call(t, n, t, e);
        /*!
 * jQuery Cookie Plugin v1.3.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
        void 0 === n || (e.exports = n)
    },
    "./src/3rd/md5/md5.js": function(e, t, n) {
        "use strict";
        n = function(e, t, n) {
            function p(e, t) {
                var n = (65535 & e) + (65535 & t);
                return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
            }
            function a(e, t, n, o, r, i) {
                return p((t = p(p(t, e), p(o, i))) << r | t >>> 32 - r, n)
            }
            function l(e, t, n, o, r, i, s) {
                return a(t & n | ~t & o, e, t, r, i, s)
            }
            function m(e, t, n, o, r, i, s) {
                return a(t & o | n & ~o, e, t, r, i, s)
            }
            function f(e, t, n, o, r, i, s) {
                return a(t ^ n ^ o, e, t, r, i, s)
            }
            function g(e, t, n, o, r, i, s) {
                return a(n ^ (t | ~o), e, t, r, i, s)
            }
            function s(e, t) {
                e[t >> 5] |= 128 << t % 32,
                e[14 + (t + 64 >>> 9 << 4)] = t;
                for (var n, o, r, d, i = 1732584193, s = -271733879, a = -1732584194, c = 271733878, u = 0; u < e.length; u += 16)
                    i = l(n = i, o = s, r = a, d = c, e[u], 7, -680876936),
                    c = l(c, i, s, a, e[u + 1], 12, -389564586),
                    a = l(a, c, i, s, e[u + 2], 17, 606105819),
                    s = l(s, a, c, i, e[u + 3], 22, -1044525330),
                    i = l(i, s, a, c, e[u + 4], 7, -176418897),
                    c = l(c, i, s, a, e[u + 5], 12, 1200080426),
                    a = l(a, c, i, s, e[u + 6], 17, -1473231341),
                    s = l(s, a, c, i, e[u + 7], 22, -45705983),
                    i = l(i, s, a, c, e[u + 8], 7, 1770035416),
                    c = l(c, i, s, a, e[u + 9], 12, -1958414417),
                    a = l(a, c, i, s, e[u + 10], 17, -42063),
                    s = l(s, a, c, i, e[u + 11], 22, -1990404162),
                    i = l(i, s, a, c, e[u + 12], 7, 1804603682),
                    c = l(c, i, s, a, e[u + 13], 12, -40341101),
                    a = l(a, c, i, s, e[u + 14], 17, -1502002290),
                    i = m(i, s = l(s, a, c, i, e[u + 15], 22, 1236535329), a, c, e[u + 1], 5, -165796510),
                    c = m(c, i, s, a, e[u + 6], 9, -1069501632),
                    a = m(a, c, i, s, e[u + 11], 14, 643717713),
                    s = m(s, a, c, i, e[u], 20, -373897302),
                    i = m(i, s, a, c, e[u + 5], 5, -701558691),
                    c = m(c, i, s, a, e[u + 10], 9, 38016083),
                    a = m(a, c, i, s, e[u + 15], 14, -660478335),
                    s = m(s, a, c, i, e[u + 4], 20, -405537848),
                    i = m(i, s, a, c, e[u + 9], 5, 568446438),
                    c = m(c, i, s, a, e[u + 14], 9, -1019803690),
                    a = m(a, c, i, s, e[u + 3], 14, -187363961),
                    s = m(s, a, c, i, e[u + 8], 20, 1163531501),
                    i = m(i, s, a, c, e[u + 13], 5, -1444681467),
                    c = m(c, i, s, a, e[u + 2], 9, -51403784),
                    a = m(a, c, i, s, e[u + 7], 14, 1735328473),
                    i = f(i, s = m(s, a, c, i, e[u + 12], 20, -1926607734), a, c, e[u + 5], 4, -378558),
                    c = f(c, i, s, a, e[u + 8], 11, -2022574463),
                    a = f(a, c, i, s, e[u + 11], 16, 1839030562),
                    s = f(s, a, c, i, e[u + 14], 23, -35309556),
                    i = f(i, s, a, c, e[u + 1], 4, -1530992060),
                    c = f(c, i, s, a, e[u + 4], 11, 1272893353),
                    a = f(a, c, i, s, e[u + 7], 16, -155497632),
                    s = f(s, a, c, i, e[u + 10], 23, -1094730640),
                    i = f(i, s, a, c, e[u + 13], 4, 681279174),
                    c = f(c, i, s, a, e[u], 11, -358537222),
                    a = f(a, c, i, s, e[u + 3], 16, -722521979),
                    s = f(s, a, c, i, e[u + 6], 23, 76029189),
                    i = f(i, s, a, c, e[u + 9], 4, -640364487),
                    c = f(c, i, s, a, e[u + 12], 11, -421815835),
                    a = f(a, c, i, s, e[u + 15], 16, 530742520),
                    i = g(i, s = f(s, a, c, i, e[u + 2], 23, -995338651), a, c, e[u], 6, -198630844),
                    c = g(c, i, s, a, e[u + 7], 10, 1126891415),
                    a = g(a, c, i, s, e[u + 14], 15, -1416354905),
                    s = g(s, a, c, i, e[u + 5], 21, -57434055),
                    i = g(i, s, a, c, e[u + 12], 6, 1700485571),
                    c = g(c, i, s, a, e[u + 3], 10, -1894986606),
                    a = g(a, c, i, s, e[u + 10], 15, -1051523),
                    s = g(s, a, c, i, e[u + 1], 21, -2054922799),
                    i = g(i, s, a, c, e[u + 8], 6, 1873313359),
                    c = g(c, i, s, a, e[u + 15], 10, -30611744),
                    a = g(a, c, i, s, e[u + 6], 15, -1560198380),
                    s = g(s, a, c, i, e[u + 13], 21, 1309151649),
                    i = g(i, s, a, c, e[u + 4], 6, -145523070),
                    c = g(c, i, s, a, e[u + 11], 10, -1120210379),
                    a = g(a, c, i, s, e[u + 2], 15, 718787259),
                    s = g(s, a, c, i, e[u + 9], 21, -343485551),
                    i = p(i, n),
                    s = p(s, o),
                    a = p(a, r),
                    c = p(c, d);
                return [i, s, a, c]
            }
            function c(e) {
                for (var t = "", n = 0; n < 32 * e.length; n += 8)
                    t += String.fromCharCode(e[n >> 5] >>> n % 32 & 255);
                return t
            }
            function u(e) {
                var t, n = [];
                for (n[(e.length >> 2) - 1] = void 0,
                t = 0; t < n.length; t += 1)
                    n[t] = 0;
                for (t = 0; t < 8 * e.length; t += 8)
                    n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
                return n
            }
            function o(e) {
                for (var t, n = "0123456789abcdef", o = "", r = 0; r < e.length; r += 1)
                    t = e.charCodeAt(r),
                    o += n.charAt(t >>> 4 & 15) + n.charAt(15 & t);
                return o
            }
            function d(e) {
                return unescape(encodeURIComponent(e))
            }
            function r(e) {
                return c(s(u(e = d(e)), 8 * e.length))
            }
            function i(e, t) {
                var n, e = d(e), t = d(t), o = u(e), r = [], i = [];
                for (r[15] = i[15] = void 0,
                16 < o.length && (o = s(o, 8 * e.length)),
                n = 0; n < 16; n += 1)
                    r[n] = 909522486 ^ o[n],
                    i[n] = 1549556828 ^ o[n];
                return e = s(r.concat(u(t)), 512 + 8 * t.length),
                c(s(i.concat(e), 640))
            }
            n.exports = function(e, t, n) {
                return t ? n ? i(t, e) : o(i(t, e)) : n ? r(e) : o(r(e))
            }
        }
        .call(t, n, t, e);
        void 0 === n || (e.exports = n)
    },
    "./src/3rd/utils/comm_report.js": function(e, t, n) {
        var o = n("./src/mmbizweb-web2-common/modules/utils/cgi.js")
          , r = n("./src/mmbizweb-web2-common/biz_common/utils/comm_report.js");
        e.exports = {
            report: function(e, t, n) {
                r.report("web", o, e, t, n)
            },
            leaveReport: function(e, t) {
                r.leaveReport("web", o, e, t)
            }
        }
    },
    "./src/3rd/wxgspeedsdk/wxgspeedsdk.js": function(e, t, n) {
        n = function(e) {
            var d, p = {};
            function i(e, t, n) {
                p[e] = p[e] || [],
                p[e][t] = p[e][t] || [],
                n < 0 || (t < 21 ? p[e][t][0] = n : p[e][t].push(n))
            }
            function s(e) {
                if (e && e.pid)
                    return e.pid + "_" + (e.uin || 0) + "_" + (e.rid || 0);
                console && console.error("Must provide a pid")
            }
            var t = [];
            function n(e) {
                "complete" == document.readyState ? e() : t.push(e)
            }
            function o() {
                for (var e = 0; e < t.length; e++)
                    t[e]();
                t = []
            }
            return window.addEventListener ? window.addEventListener("load", o, !1) : window.attachEvent && window.attachEvent("onload", o),
            {
                saveSpeeds: function(e) {
                    if (!e.pid || !e.speeds)
                        return -1;
                    0 < !e.speeds.length && (t = e.speeds,
                    e.speeds = [],
                    e.speeds.push(t)),
                    e.user_define && (d = e.user_define);
                    for (var t, n = s(e), o = 0; o < e.speeds.length; o++) {
                        var r = e.speeds[o];
                        r.time = parseInt(r.time),
                        20 < r.sid && 0 <= r.time && i(n, r.sid, r.time)
                    }
                },
                send: function() {
                    n(function() {
                        setTimeout(function() {
                            for (var e in p) {
                                u = c = a = s = i = r = o = o = n = t = void 0;
                                var t = {
                                    pid_uin_rid: e,
                                    speeds: p[e],
                                    user_define: d
                                }
                                  , n = "https://badjs.weixinbridge.com/frontend/reportspeed?";
                                if (3 == (o = t.pid_uin_rid.split("_")).length) {
                                    for (var o = "pid=" + o[0] + "&uin=" + o[1] + "&rid=" + o[2], r = (t.user_define && (o += "&user_define=" + t.user_define),
                                    n + o + "&speeds="), i = "", s = [], a = 1; a < t.speeds.length; a++)
                                        if (t.speeds[a]) {
                                            for (var c = 0; c < t.speeds[a].length; c++) {
                                                var u = a + "_" + t.speeds[a][c];
                                                i = r.length + i.length + u.length < 1024 ? i + u + ";" : (i.length && s.push(r + i.substring(0, i.length - 1)),
                                                u + ";")
                                            }
                                            a == t.speeds.length - 1 && s.push(r + i.substring(0, i.length - 1))
                                        }
                                    for (a = 0; a < s.length; a++)
                                        (new Image).src = s[a]
                                } else
                                    console && console.error("pid,uin,rid, invalid args")
                            }
                            p = {}
                        }, 100)
                    })
                },
                setFirstViewTime: function(e) {
                    n(function() {
                        if (!e.pid || !e.time)
                            return -1;
                        i(s(e), 9, e.time)
                    })
                },
                setBasicTime: function(o) {
                    n(function() {
                        var e, t = s(o), n = (p[t] || (p[t] = []),
                        window.performance || window.msPerformance || window.webkitPerformance || {});
                        n && n.timing && (e = n.timing || {},
                        i(t, 1, e.domainLookupEnd - e.domainLookupStart),
                        i(t, 2, "https:" == location.protocol && 0 != e.secureConnectionStart ? e.connectEnd - e.secureConnectionStart : 0),
                        i(t, 3, e.connectEnd - e.connectStart),
                        i(t, 4, e.responseStart - e.requestStart),
                        i(t, 5, e.responseEnd - e.responseStart),
                        i(t, 6, e.domContentLoadedEventStart - e.domLoading),
                        i(t, 7, 0 == e.domComplete ? 0 : e.domComplete - e.domLoading),
                        i(t, 8, 0 == e.loadEventEnd ? 0 : e.loadEventEnd - e.loadEventStart),
                        setTimeout(function() {
                            e.loadEventEnd && (i(t, 7, 0 == e.domComplete ? 0 : e.domComplete - e.domLoading),
                            i(t, 8, 0 == e.loadEventEnd ? 0 : e.loadEventEnd - e.loadEventStart))
                        }, 0),
                        p[t][9] || i(t, 9, e.domContentLoadedEventStart - e.navigationStart),
                        i(t, 10, e.redirectEnd - e.redirectStart),
                        i(t, 11, e.domainLookupStart - e.fetchStart),
                        i(t, 12, e.domLoading - e.responseStart))
                    })
                }
            }
        }
        .call(t, n, t, e);
        void 0 === n || (e.exports = n)
    },
    "./src/mmbizweb-web2-common/biz_common/utils/comm_report.js": function(e, t, n) {
        n = function() {
            function r(e, t) {
                return (t = JSON.parse(JSON.stringify(t))).log_id = e,
                JSON.stringify(t)
            }
            function i(t, n, o) {
                return function(e) {
                    e && 0 !== e.err_code && console.warn("[comm_report] report " + t + " fail: ", e.err_msg, n),
                    "function" == typeof o.success && o.success(e)
                }
            }
            function s(n, o, r) {
                return function(e, t) {
                    console.error("[comm_report] report " + n + " error: ", t, o),
                    "function" == typeof r.error && r.error(e, t)
                }
            }
            var a = {
                web: {
                    report: "/cgi-bin/webreport"
                },
                wap: {
                    report: "/mp/wapcommreport"
                }
            }
              , c = !1
              , u = []
              , d = {
                web: {
                    report: function(e, t, n, o) {
                        o = o || {},
                        e.post({
                            url: a.web.report,
                            data: {
                                reportjson: r(t, n)
                            },
                            async: o.async,
                            success: i(t, n, o),
                            error: s(t, n, o)
                        })
                    },
                    leaveReport: function(e, t, n) {
                        var o;
                        u.push([e, t, n]),
                        c || (o = !(c = !0),
                        e = function() {
                            o || (o = !0,
                            u.forEach(function(e) {
                                d.web.report(e[0], e[1], e[2])
                            }))
                        }
                        ,
                        window.addEventListener("beforeunload", e, !1),
                        window.addEventListener("unload", e, !1))
                    }
                },
                wap: {
                    report: function(e, t, n, o) {
                        o = o || {},
                        e({
                            type: "POST",
                            dataType: "json",
                            url: a.wap.report,
                            data: {
                                reportjson: r(t, n)
                            },
                            async: o.async,
                            success: i(t, n, o),
                            error: s(t, n, o)
                        })
                    }
                }
            };
            return {
                report: function(e, t, n, o, r) {
                    d[e].report(t, n, o, r)
                },
                leaveReport: function(e, t, n, o) {
                    d[e].leaveReport(t, n, o)
                },
                getUrl: function(e, t) {
                    return a[e][t]
                },
                getData: function(e, t, n) {
                    e = r(e, t);
                    return "reportjson=" + (e = n ? encodeURIComponent(e) : e)
                }
            }
        }
        .call(t, n, t, e);
        void 0 === n || (e.exports = n)
    },
    "./src/mmbizweb-web2-common/modules/utils/ajax.js": function(e, t) {
        function l(e) {
            return (l = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                return typeof e
            }
            : function(e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            }
            )(e)
        }
        function m() {}
        e.exports = function(n) {
            var e = (n.type || "GET").toUpperCase()
              , t = n.url
              , d = void 0 === n.async || n.async
              , o = new XMLHttpRequest
              , r = (o.donotHock = !!n.donotHock,
            o.withCredentials = !0,
            n.responseType && (o.responseType = n.responseType),
            null)
              , i = null
              , p = m
              , s = m
              , a = m;
            if (n.success && (p = function(e) {
                try {
                    n.success(e)
                } catch (e) {
                    throw e
                }
            }
            ),
            n.error && (s = function(e, t) {
                try {
                    n.error(e, t)
                } catch (e) {
                    throw e
                }
            }
            ),
            n.complete && (a = function() {
                try {
                    n.complete()
                } catch (e) {
                    throw e
                }
            }
            ),
            "object" === l(n.data)) {
                var c, u = n.data, i = [];
                for (c in u)
                    Object.prototype.hasOwnProperty.call(u, c) && i.push(c + "=" + encodeURIComponent(u[c]));
                i = i.join("&")
            } else
                i = "string" == typeof n.data ? n.data : null;
            "GET" === e && i && (t += (0 <= t.indexOf("?") ? "&" : "?") + i),
            o.open(e, t, d),
            o.onerror = function() {
                s(o, "error"),
                r && clearTimeout(r),
                a()
            }
            ,
            o.onreadystatechange = function() {
                if (3 === o.readyState && n.received && n.received(o),
                4 === o.readyState) {
                    o.onreadystatechange = null;
                    var e = o.status;
                    if (200 <= e && e < 400)
                        try {
                            if ("blob" === n.responseType)
                                t = o.response;
                            else {
                                var t = o.responseText;
                                if ("json" === n.dataType)
                                    try {
                                        t = JSON.parse(t)
                                    } catch (e) {
                                        return void s(o, "parsererror")
                                    }
                            }
                            p(t)
                        } catch (e) {
                            throw e
                        }
                    else
                        s(o, "error");
                    r && clearTimeout(r),
                    a(),
                    a = m
                }
            }
            ,
            "POST" === e && o.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"),
            n.crossDomain || o.setRequestHeader("X-Requested-With", "XMLHttpRequest"),
            void 0 !== n.timeout && (r = setTimeout(function() {
                o.abort("timeout"),
                a(),
                a = m
            }, n.timeout));
            try {
                o.send(i)
            } catch (e) {
                s(o, "timeout")
            }
        }
    },
    "./src/mmbizweb-web2-common/modules/utils/cgi.js": function(e, n, t) {
        function r(e) {
            for (var t = e || {}, n = Object.keys(a), o = 0; o < n.length; o++)
                t[n[o]] = a[n[o]];
            return t
        }
        function i(e, t) {
            var n = -1 !== location.href.indexOf("/cgi-bin/home") && (-1 !== t.url.indexOf("/misc/safeassistant") || -1 !== t.url.indexOf("/safe/safeuuid"))
              , o = 11;
            switch (e) {
            case "timeout":
                o = 7;
                break;
            case "error":
                o = 8;
                break;
            case "notmodified":
                o = 9;
                break;
            case "parsererror":
                o = 10;
                break;
            default:
                o = 11
            }
            for (var r = ["lang", "random", "f", "ajax", "token"], i = 0; i < r.length; ++i) {
                var s = r[i];
                t.data && t.data[s] && delete t.data[s]
            }
            o += n ? 100 : 0;
            var a = ""
              , a = /selfcheck/.test(t.url) ? t.data && t.data.AppMsgId : JSON.stringify(t.data).substr(0, 50);
            c({
                url: "/misc/jslog?1=1",
                data: {
                    content: u.format("[fakeid={uin}] [xhr] [url={url}] [param={param}] [info={info}] [useragent={useragent}] [page={page}]", {
                        uin: d.uin,
                        useragent: window.navigator.userAgent,
                        page: location.href,
                        url: t.url,
                        param: a,
                        info: e
                    }),
                    id: o,
                    level: "error"
                },
                type: "POST"
            }),
            c({
                url: "/misc/jslog?1=1",
                data: {
                    content: u.format("[fakeid={uin}] [xhr] [url={url}] [param={param}] [info={info}] [useragent={useragent}] [page={page}]", {
                        uin: d.uin,
                        useragent: window.navigator.userAgent,
                        page: location.href,
                        url: t.url,
                        param: a,
                        info: e
                    }),
                    id: 6 + (n ? 100 : 0),
                    level: "error"
                },
                type: "POST"
            }),
            "timeout" !== e || t.notShowTimeoutErr || Vue.prototype.$tipsErr("你的网络环境较差，请稍后重试")
        }
        function s(e, i) {
            var s = e;
            return "function" != typeof s && (s = function() {}
            ),
            e = function(e) {
                try {
                    var t, n, o = s.toString(), r = {
                        uin: d.uin || "0",
                        id: "64430",
                        key: "0",
                        url: "",
                        location: encodeURIComponent(window.location.href) || "",
                        ret: e && e.base_resp && e.base_resp.ret || "undefined"
                    };
                    e && e.base_resp && 0 !== e.base_resp.ret && (o.indexOf("handleRet") < 0 && o.indexOf(e.base_resp.ret) < 0 && ((new Image).src = u.format("https://badjs.weixinbridge.com/badjs?level=4&uin={uin}&id={id}&msg={msg}&from={url}", {
                        uin: r.uin,
                        url: r.url || r.location,
                        id: 138,
                        msg: encodeURIComponent("ret=" + r.ret + "|idkey=" + r.id + ":" + r.key)
                    })),
                    void 0 !== window.WX_BJ_REPORT && window.WX_BJ_REPORT.BadJs && (t = "",
                    -1 !== i.indexOf("?") ? (t = i.substr(0, i.indexOf("?")),
                    (n = p.parseQuery(i)).action && (t += "?action=".concat(n.action))) : t = i,
                    window.WX_BJ_REPORT.BadJs.report(t, "ret=".concat(e.base_resp.ret), {
                        mid: window.PAGE_MID,
                        view: "web_retcode"
                    })))
                } catch (e) {
                    console.error(e)
                }
                s(e)
            }
        }
        var c = t("./src/mmbizweb-web2-common/modules/utils/ajax.js")
          , u = t("./src/mmbizweb-web2-common/modules/utils/str_util.js")
          , o = t("./src/mmbizweb-web2-common/modules/utils/object.js")
          , p = t("./src/mmbizweb-web2-common/modules/utils/url.js")
          , d = (window.wx.commonData || window.wx).data
          , a = {
            token: d.t,
            lang: d.lang,
            f: "json",
            ajax: "1"
        }
          , l = {
            0: "恭喜你，操作成功！",
            "-1": "系统错误，请稍后尝试。",
            200002: "参数错误，请核对参数后重试。",
            200003: "登录超时，请重新登录。",
            200004: "请求页面的域名没有授权。",
            200005: "请求方式错误，请确认请求方式后重试。",
            200006: "表单名称验证出错，请核对表单名称后重试。",
            200007: "登录超时，请重新登录。",
            200040: "登录超时，请重新登录。"
        }
          , t = {
            updateCommonPostData: function() {
                a = {
                    token: d.data.t,
                    lang: d.lang,
                    f: "json",
                    ajax: "1"
                }
            },
            get: function(n, e, o, t) {
                n.data = r(n.data),
                n.success = n.success || e,
                n.complete = n.complete || t,
                o = n.error || o,
                n.error = function(e, t) {
                    i(t, n),
                    o && o(e, t)
                }
                ,
                n.dataType = "json",
                n.success = s(n.success, n.url),
                c(n)
            },
            post: function(n, e, o, t) {
                n.type = "POST",
                n.data = r(n.data),
                n.success = n.success || e,
                n.complete = n.complete || t,
                o = n.error || o,
                n.error = function(e, t) {
                    i(t, n),
                    o && o(e, t)
                }
                ,
                n.dataType = "json",
                n.success = s(n.success, n.url),
                c(n)
            },
            handleRet: function(e, t) {
                var n = {
                    msg: t.msg || "系统繁忙，请稍后尝试"
                };
                return e && e.base_resp && e.base_resp.ret && (t = o.clone(t, !0),
                (t = Object.assign({
                    uin: d.uin || "0",
                    id: "64430",
                    key: "0",
                    url: "",
                    location: encodeURIComponent(window.location.href) || "",
                    ret: e.base_resp.ret,
                    showMsg: !0,
                    msg: "系统繁忙，请稍后尝试"
                }, t)).url = encodeURIComponent(t.url),
                (e = l[t.ret]) ? (t.showMsg && Vue.prototype.$tipsErr(e),
                n.msg = e) : ((new Image).src = u.format("/mp/unknow_ret_report?uin={uin}&id={id}&key={key}&url={url}&location={location}&ret={ret}&method=get&action=report", t),
                t.showMsg && Vue.prototype.$tipsErr(t.msg),
                (new Image).src = u.format("/mp/unknow_ret_report?uin={uin}&id=64430&key=126&url={url}&location={location}&ret={ret}&method=get&action=report", t),
                (new Image).src = u.format("https://badjs.weixinbridge.com/badjs?level=4&uin={uin}&id={id}&msg={msg}&from={url}", {
                    uin: t.uin,
                    url: t.url || t.location,
                    id: 138,
                    msg: encodeURIComponent("ret=" + t.ret + "|idkey=" + t.id + ":" + t.key)
                }))),
                n
            }
        };
        e.exports = t
    },
    "./src/mmbizweb-web2-common/modules/utils/contributions.js": function(e, t, n) {
        n = n("./src/mmbizweb-web2-common/modules/utils/contributors.js").sort(function(e, t) {
            return e.localeCompare(t)
        }).join(", ");
        window.PAGE_MID && window.PAGE_MID.indexOf("loginpage") < 0 && !window.thanksToContributor && (console.info("%c 感谢大家为微信公众号做出的卓越贡献", "background: url(https://res.wx.qq.com/mpres/zh_CN/htmledition/weui-desktopSkin-common/svg/buildless/new_bg_logo_primary.svg) no-repeat; padding: 10px 130px 10px 130px; font-family: helvetica; font-size: 20px; line-height: 12px;"),
        console.info("%c Contributors: ".concat(n), "font-family: consolas; font-size: 10px;"),
        console.info("%c ", "background: url(https://mmbiz.qlogo.cn/mmbiz_png/aOncaiaP23TAeVMJdplptU1Tv7sKs8WcuU7icS1UMXGialyr2I8qRiakTeiaLxlQjx64OWZohASfThklfOL76phQz5A/0?wx_fmt=png) no-repeat; background-size: 160px 100px; padding: 50px 80px"),
        console.info("%c 愿大家出走半生，归来仍是少年", "font-family: helvetica; font-size: 8px; text-align: right;"),
        window.thanksToContributor = !0)
    },
    "./src/mmbizweb-web2-common/modules/utils/contributors.js": function(e, t) {
        e.exports = ["dididong", "yinshen", "semineli", "fangzhan", "starszhou", "hongfenglin", "coenwang", "tommyjqliu"]
    },
    "./src/mmbizweb-web2-common/modules/utils/object.js": function(e, d) {
        var t = "[object Array]"
          , n = "[object Object]"
          , o = Object.prototype.toString
          , r = Object.prototype.hasOwnProperty;
        function s(e, t) {
            return r.call(e, t)
        }
        function a(e, t) {
            for (var n in t)
                s(t, n) && (e[n] = t[n]);
            return e
        }
        function c(e) {
            return o.call(e) === n
        }
        function u(e) {
            return o.call(e) === t
        }
        var i = null;
        var i = "function" == typeof Number.isFinite ? Number.isFinite.bind(Number) : "function" == typeof window.isFinite ? window.isFinite : function() {
            return !0
        }
          , p = null
          , p = "function" == typeof Object.assign ? Object.assign : function() {
            if (null == (arguments.length <= 0 ? void 0 : arguments[0]))
                throw new TypeError("Cannot convert undefined or null to object");
            for (var e = Object(arguments.length <= 0 ? void 0 : arguments[0]), t = 1; t < arguments.length; t++) {
                var n = t < 0 || arguments.length <= t ? void 0 : arguments[t];
                if (null != n)
                    for (var o in n)
                        s(n, o) && (e[o] = n[o])
            }
            return e
        }
        ;
        e.exports = {
            assign: p,
            extend: a,
            clone: function e(t, n) {
                var o;
                if (!0 !== n)
                    return a({}, t);
                if (u(t))
                    for (var r in o = [],
                    t)
                        s(t, r) && (c(t[r]) ? o.push(e(t[r], !0)) : o.push(t[r]));
                else
                    for (var i in o = {},
                    t)
                        s(t, i) && (c(t[i]) ? o[i] = e(t[i], !0) : o[i] = t[i]);
                return o
            },
            isObject: c,
            isElement: function(e) {
                return !(!this || 1 !== e.nodeType)
            },
            isArray: u,
            isFunction: function(e) {
                return "function" == typeof e
            },
            isString: function(e) {
                return "[object String]" === o.call(e)
            },
            isBoolean: function(e) {
                return "[object Boolean]" === o.call(e)
            },
            isNumber: function(e) {
                return "[object Number]" === o.call(e)
            },
            isDate: function(e) {
                return "[object Date]" === o.call(e)
            },
            isUndefined: function(e) {
                return void 0 === e
            },
            isRepExp: function(e) {
                return "[object RegExp]" === o.call(e)
            },
            isFinite: i,
            param: function(e, t) {
                var n, o = [];
                for (n in e)
                    s(e, n) && (!0 === t ? o.push([encodeURIComponent(n), "=", encodeURIComponent(e[n]), "&"].join("")) : o.push([n, "=", e[n], "&"].join("")));
                return o.join("").slice(0, -1)
            },
            each: function(e, t) {
                if (void 0 !== t)
                    for (var n in e)
                        if (s(e, n) && !1 === t(e[n], n))
                            break
            },
            hasOwn: s
        }
    },
    "./src/mmbizweb-web2-common/modules/utils/str_util.js": function(e, t) {
        e.exports = {
            escape2Html: function(e) {
                var n = {
                    lt: "<",
                    gt: ">",
                    nbsp: " ",
                    amp: "&",
                    quot: '"'
                };
                return e.replace(/&(lt|gt|nbsp|amp|quot);/gi, function(e, t) {
                    return n[t]
                })
            },
            format: function(e, n) {
                return e.replace(/\{(\w+)\}/g, function(e, t) {
                    return void 0 !== n[t] ? n[t] : e
                })
            },
            sprintf: function() {
                for (var e, t = arguments.length, n = new Array(t), o = 0; o < t; o++)
                    n[o] = arguments[o];
                var r, i, s = n[0] || "", a = n.length - 1;
                if (a < 1)
                    return s;
                for (e = 1; e < 1 + a; )
                    s = s.replace(/%s/, "{#" + e + "#}"),
                    e++;
                for (s.replace("%s", ""),
                e = 1; ; ) {
                    if (void 0 === (r = n[e]))
                        break;
                    i = new RegExp("{#" + e + "#}","g"),
                    s = s.replace(i, r),
                    e++
                }
                return s
            },
            text: function(e) {
                return e.replace(/<\/?[^>]*\/?>/g, "")
            },
            len: function(e) {
                return e.replace(/[^\x00-\xff]/g, "**").length
            },
            truncate: function(e, t, n) {
                t = t || 30,
                n = Object.isUndefined(n) ? "..." : n;
                return e.length > t ? e.slice(0, t - n.length) + n : String(e)
            },
            trim: String.prototype.trim || function(e, t) {
                return !0 === t ? e.replace(/^\s+/, "") : (!1 === t ? e : e.replace(/^\s+/, "")).replace(/\s+$/, "")
            }
            ,
            html: function(e, t) {
                for (var n = !1 === t ? ["&#39;", "'", "&quot;", '"', "&nbsp;", " ", "&gt;", ">", "&lt;", "<", "&amp;", "&"] : ["&", "&amp;", "<", "&lt;", ">", "&gt;", " ", "&nbsp;", '"', "&quot;", "'", "&#39;"], o = e, r = 0; r < n.length; r += 2)
                    o = o.replace(new RegExp(n[r],"g"), n[1 + r]);
                return o
            },
            has: function(e, t) {
                return -1 < e.indexOf(t)
            },
            startsWith: function(e, t) {
                return 0 === e.lastIndexOf(t, 0)
            },
            endsWith: function(e, t) {
                var n = e.length - t.length;
                return 0 <= n && e.indexOf(t, n) === n
            },
            param: function(e, t, n) {
                var o;
                return "function" == typeof e.split ? (e = e.split(n || "&"),
                o = {},
                e.each(function(e) {
                    e = e.split("=");
                    2 === e.length && e[0] && e[1] && (!0 === t ? o[decodeURIComponent(e[0])] = decodeURIComponent(e[1]) : o[e[0]] = e[1])
                }),
                o) : null
            },
            empty: function(e) {
                return "" === e
            },
            blank: function(e) {
                return /^\s*$/.test(e)
            },
            bytes: function(e) {
                for (var t, n = 0, o = 0; t = e.charAt(n++); )
                    o += t.charCodeAt().toString(16).length / 2;
                return o
            }
        }
    },
    "./src/mmbizweb-web2-common/modules/utils/url.js": function(e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        }),
        t.addBaseParm = function(e) {
            if (!e)
                return "";
            if (0 === e.indexOf("javasript:"))
                return e;
            var t = window.wx.commonData.data
              , n = e.charAt(e.length - 1);
            "?" !== n && (-1 === e.indexOf("?") ? e += "?" : "&" !== n && (e += "&"));
            return e + "token=" + t.t + "&lang=" + t.lang
        }
        ,
        t.fullUrl = function(e) {
            if (!e)
                return "";
            if (0 === e.indexOf("javasript:"))
                return e;
            var t = wx.commonData.data.param;
            return -1 !== e.indexOf("?") ? e + t : e + "?1=1" + t
        }
        ,
        t.parseQuery = function(e) {
            var t = {}
              , n = e.match(/[?&]([^=&#]+)=([^&#]*)/g);
            if (n)
                for (var o in n) {
                    var r;
                    Object.prototype.hasOwnProperty.call(n, o) && (o = n[o].split("="),
                    r = o[0].substr(1),
                    o = o[1],
                    t[r] ? t[r] = [].concat(t[r], o) : t[r] = o)
                }
            return t
        }
    },
    "./src/pages/login/loginpage/loginpage.js": function(d, p, e) {
        function t(e) {
            return (t = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                return typeof e
            }
            : function(e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            }
            )(e)
        }
        function n(t, e) {
            var n, o = Object.keys(t);
            return Object.getOwnPropertySymbols && (n = Object.getOwnPropertySymbols(t),
            e && (n = n.filter(function(e) {
                return Object.getOwnPropertyDescriptor(t, e).enumerable
            })),
            o.push.apply(o, n)),
            o
        }
        var r = e("./src/mmbizweb-web2-common/modules/utils/cgi.js")
          , l = e("./src/pages/modules/utils/get_cgi_data.js")
          , m = e("./src/pages/modules/utils/get_custom_service.js")
          , f = e("./src/3rd/md5/md5.js")
          , u = e("./src/3rd/cookie/cookie.js")
          , g = e("./node_modules/vuex/dist/vuex.esm.js")
          , h = e("./src/3rd/utils/comm_report.js")
          , s = e("./src/3rd/editor/common/monitor.js")
          , b = e("./src/pages/modules/faq/faq_hover/faq_hover.js")
          , w = e("./src/3rd/wxgspeedsdk/wxgspeedsdk.js")
          , _ = e("./src/pages/modules/utils/object.js").assign
          , v = e("./src/pages/modules/utils/report.js").idkey
          , y = e("./src/pages/modules/base/base.js")
          , x = (e("./src/pages/login/loginpage/style/loginpage.less"),
        e("./src/pages/login/loginpage/style/loginpage.en_US.less"),
        e("./src/pages/modules/safe_input/safe_input.js"))
          , o = l("pages/login/loginpage")
          , i = "loginMode"
          , j = 0
          , k = 0
          , S = (navigator && !navigator.cookieEnabled && (j = 1),
        window.localStorage && !window.localStorage.getItem(i) && (k = 1),
        0);
        try {
            setTimeout(function() {
                var e;
                (e = document.createElement("script")).onload = function() {
                    S = 1,
                    document.body.removeChild(e)
                }
                ,
                e.src = "chrome-extension://kjmjndilfndibkgdfkekhnbnmiifcpjk/resource/jsencrypt.min.js",
                document.body.appendChild(e)
            }, 200)
        } catch (e) {}
        function a(e) {
            return e <= 3 ? 1500 : 3 < e && e <= 30 ? 1e3 : 30 < e && e <= 50 ? 1500 : 2e3
        }
        var c = null
          , c = new y({
            el: "#app",
            store: new g.Store({
                modules: {
                    main: {
                        state: {
                            step: 0,
                            mode: window.wx.cgiData.defaultScanlogin ? 1 : +(localStorage.getItem(i) || 1),
                            qrcodeSrc: "",
                            scanLoginType: 0,
                            bizList: [],
                            wxList: [],
                            activeBizIndex: 0,
                            activeWxIndex: -1,
                            state: "state_waiting",
                            rejectWxList: [],
                            currentLang: "" === o.currentLang ? "zh_CN" : o.currentLang,
                            err: "",
                            verifyImg: "",
                            isNeedVerify: !1,
                            account: "",
                            rememberCheck: !1,
                            pwd: "",
                            verify: ""
                        },
                        mutations: {
                            _sucGetIngorePassList: function(n, e) {
                                n.bizList = e.ignor_passwd_list,
                                n.bizList.forEach(function(e, t) {
                                    n.rejectWxList.push([]),
                                    n.bizList[t].userlist.forEach(function() {
                                        n.rejectWxList[t].push(!1)
                                    })
                                }),
                                n.step = 1,
                                c.report19015({
                                    optype: 1,
                                    page_state: 2
                                })
                            },
                            _setLanguage: function(e, t) {
                                var n, o = window.location.host, r = window.location.protocol, i = window.location.pathname, s = window.location.hash, a = function() {
                                    var e, t, n = window.location.search.substring(1).split("&"), o = {};
                                    for (t in n)
                                        "" !== n[t] && n[t].split && (e = n[t].split("="),
                                        o[decodeURIComponent(e[0])] = decodeURIComponent(e[1]));
                                    return o
                                }(), c = [];
                                for (n in a.lang = t.currentLang,
                                a)
                                    a[n] && c.push([encodeURIComponent(n), encodeURIComponent(a[n])].join("="));
                                r = r + "//" + o + i + "?" + c.join("&") + s;
                                u.cookie("mm_lang", t.currentLang, {
                                    expires: 30,
                                    path: "/"
                                }),
                                e.currentLang = t.currentLang,
                                window.openUrl(r)
                            },
                            _loginCallback: function(e, t) {
                                var n, o = t.json, r = "";
                                switch (o.base_resp.ret) {
                                case 0:
                                    localStorage.setItem(i, e.mode),
                                    u.cookie("noticeLoginFlag", 1, {
                                        expires: 30
                                    }),
                                    e.rememberCheck ? u.cookie("remember_acct", e.account, {
                                        expires: 30
                                    }) : u.remove("remember_acct"),
                                    /\/cgi-bin\/home\?/.test(o.redirect_url) ? -1 < window.location.href.indexOf("toUrl=ad") && ((n = o.redirect_url.match(/token=(\d*)/)) && n[1] && (o.redirect_url = "/promotion/advertiser_index?lang=zh_CN&token=" + n[1] + "&aSource=" + (window.aSource || ""))) : /\/cgi-bin\/readtemplate\?t=user\/validate_wx_tmpl/.test(o.redirect_url) && -1 < window.location.href.indexOf("toUrl=ad") && (o.redirect_url += "&toUrl=ad&aSource=" + (window.aSource || "")),
                                    window.openUrl(o.redirect_url);
                                    break;
                                case -1:
                                    r = "系统错误，请稍候再试。";
                                    break;
                                case 200002:
                                    r = "帐号或密码错误。";
                                    break;
                                case 200007:
                                    r = "您目前处于访问受限状态。";
                                    break;
                                case 200008:
                                    e.isNeedVerify = !0,
                                    r = "请输入图中的验证码。";
                                    break;
                                case 200021:
                                    r = "不存在该帐户。";
                                    break;
                                case 200023:
                                    r = "您输入的帐号或者密码不正确，请重新输入。";
                                    break;
                                case 200025:
                                    r = '海外帐号请在公众平台海外版登录，<a href="http://admin.wechat.com/">点击登录</a>';
                                    break;
                                case 200026:
                                    r = "该公众会议号已经过期，无法再登录使用。";
                                    break;
                                case 200027:
                                    r = "您输入的验证码不正确，请重新输入。";
                                    break;
                                case 200121:
                                    r = '该帐号属于微信开放平台，请<a href="https://open.weixin.qq.com/">点击此处</a>登录';
                                    break;
                                case 200122:
                                    r = '这是企业号帐号，现已升级为企业微信，请<a href="https://work.weixin.qq.com/wework_admin/loginpage_wx?from=mp">点击此处</a>登录';
                                    break;
                                case 250002:
                                    r = "该帐号已被注销。";
                                    break;
                                case 250003:
                                    r = '由于长时间未使用，该帐号已被系统冻结，若需要恢复，你可以点击<a href="'.concat(o.findacct_url, '">帐号找回</a>进行恢复');
                                    break;
                                case 780001:
                                    r = '公众平台将不再支持QQ帐号登录，请以邮箱帐号登录。<br/><a href="/cgi-bin/bizunbindqq?action=page&qq='.concat(o.binduin, '">前往绑定邮箱</a>');
                                    break;
                                default:
                                    r = "未知的返回。",
                                    (new Image).src = "/mp/unknow_ret_report?uin=0&id=64462&key=0&url=" + encodeURIComponent("/cgi-bin/login") + "&location=" + encodeURIComponent(window.location.href) + "&ret=" + o.base_resp.ret + "&method=get&action=report"
                                }
                                "" !== r && (e.err = r)
                            },
                            quickLogin1: function(e) {
                                var t;
                                e.wxList = e.bizList[e.activeBizIndex].userlist,
                                t = (e.wxList.length,
                                "state_chosen"),
                                e.activeWxIndex = 0,
                                e.step = 2,
                                e.state = t
                            },
                            updateReject: function(e) {
                                e.state = "state_reject",
                                e.rejectWxList[e.activeBizIndex][e.activeWxIndex] = !0,
                                e.activeWxIndex = -1,
                                e.step = 2
                            },
                            switchMode: function(e, t) {
                                e.mode = t.mode
                            },
                            switchScanLoginType: function(e, t) {
                                e.scanLoginType = t.scanLoginType
                            },
                            refreshQrcode: function(e) {
                                !1 === c.hasStartLogin ? c.getQrcode() : (!1 === c.hasStartLogin && (s.setSum(125091, 0, 1),
                                s.send()),
                                e.qrcodeSrc = "/cgi-bin/scanloginqrcode?action=getqrcode&random=".concat(+new Date),
                                c.qrcodeRefreshTimes++,
                                c.startCheckQrcode())
                            },
                            __set_state: function(e, t) {
                                for (var n in t)
                                    e[n] = t[n]
                            }
                        },
                        actions: {
                            getIngorePassList: function(t) {
                                var n = this;
                                r.post({
                                    url: "/cgi-bin/bizlogin",
                                    data: {
                                        action: "prelogin"
                                    }
                                }, function(e) {
                                    n.bizList = e.ignor_passwd_list,
                                    0 === e.base_resp.ret && 1 === e.eignor_passwd_result && 0 < n.bizList.length ? (1 === t.rootState.main.mode && c.stopCheckQrcode(),
                                    t.commit("_sucGetIngorePassList", e)) : c.report19015({
                                        optype: 1,
                                        page_state: 1 === t.rootState.main.mode ? 3 : 1
                                    })
                                })
                            },
                            setLanguage: function(e, t) {
                                e.commit("_setLanguage", t)
                            },
                            login: function(e, t) {
                                e.dispatch("_loginPost", Object.assign({
                                    isOld: !1,
                                    url: "/cgi-bin/bizlogin?action=startlogin"
                                }, t))
                            },
                            verifyImgRefresh: function(e, t) {
                                e.rootState.main.isNeedVerify,
                                e.rootState.main.isNeedVerify && e.commit("__set_state", {
                                    verifyImg: "/cgi-bin/verifycode?username=" + t.account + "&r=" + t.rand
                                })
                            },
                            _loginPost: function(t, n) {
                                r.post({
                                    url: n.url,
                                    data: {
                                        username: n.account,
                                        pwd: f(n.pwd.substr(0, 16)),
                                        imgcode: n.verify,
                                        f: "json",
                                        userlang: n.currentLang,
                                        redirect_url: o.redirectUrl
                                    }
                                }, n.isOld ? function(e) {
                                    t.commit("_loginCallback", Object.assign({
                                        json: e
                                    }, n)),
                                    0 !== e.base_resp.ret && t.dispatch("verifyImgRefresh", {
                                        account: n.account,
                                        rand: n.rand
                                    })
                                }
                                : function(e) {
                                    0 === e.grey ? ((new Image).src = "/mp/jsmonitor?idkey=66811_4_1",
                                    t.dispatch("_loginPost", Object.assign({
                                        isOld: !0,
                                        url: "/cgi-bin/login?loginhook=4"
                                    }, n))) : (t.commit("_loginCallback", Object.assign({
                                        json: e
                                    }, n)),
                                    0 !== e.base_resp.ret && t.dispatch("verifyImgRefresh", {
                                        account: n.account,
                                        rand: n.rand
                                    }))
                                }
                                )
                            },
                            quickLogin1: function(e) {
                                var t = [];
                                e.commit("quickLogin1"),
                                e.state.wxList.forEach(function(e) {
                                    t.push(e.openid)
                                }),
                                e.dispatch("quickLoginReport", {
                                    openidPost: t
                                })
                            },
                            quickLoginReport: function(e, t) {
                                r.post({
                                    url: "/cgi-bin/bizlogin",
                                    data: {
                                        action: "report",
                                        openid: t.openidPost.join("|")
                                    }
                                })
                            },
                            quickLogin2: function(e, t) {
                                e.commit("__set_state", {
                                    state: "state_login",
                                    step: 3
                                }),
                                e.dispatch("startLogin", {
                                    openid: e.state.wxList[e.state.activeWxIndex].openid,
                                    currentLang: t.currentLang
                                })
                            },
                            startLogin: function(t, n) {
                                r.post({
                                    url: "/cgi-bin/bizlogin?action=startlogin",
                                    data: {
                                        openid: n.openid,
                                        userlang: n.currentLang
                                    }
                                }, function(e) {
                                    n.inlTimes = 1,
                                    e && e.base_resp && 0 === e.base_resp.ret ? t.dispatch("polledLoginAuth", n) : e && 3 <= e.eignor_passwd_result ? t.commit("updateReject") : t.commit("__set_state", {
                                        state: "state_failed",
                                        step: 2
                                    })
                                })
                            },
                            bizLogin: function(n, e) {
                                var t = {
                                    userlang: e.currentLang,
                                    redirect_url: o.redirectUrl,
                                    cookie_forbidden: j,
                                    cookie_cleaned: k,
                                    plugin_used: S
                                };
                                e.loginType && (t.login_type = e.loginType),
                                r.post({
                                    url: "/cgi-bin/bizlogin?action=login",
                                    data: t
                                }, function(e) {
                                    var t;
                                    e && e.redirect_url ? (localStorage.setItem(i, n.state.mode),
                                    -1 < window.location.href.indexOf("toUrl=ad") && ((t = e.redirect_url.match(/token=(\d*)/)) && t[1] && (e.redirect_url = "/promotion/advertiser_index?lang=zh_CN&token=" + t[1] + "&aSource=" + (window.aSource || ""))),
                                    (new Image).src = "/misc/jslog?id=100&content=loginSuccess&level=error",
                                    window.openUrl(e.redirect_url)) : (c.$tipsErr("系统繁忙，请稍后再试"),
                                    (new Image).src = "/misc/jslog?id=99&content=loginError&level=error")
                                })
                            },
                            polledLoginAuth: function(t, n) {
                                function o() {
                                    "state_login" === t.rootState.main.state && (setTimeout(function() {
                                        n.inlTimes++,
                                        t.dispatch("polledLoginAuth", n)
                                    }, a(n.inlTimes)),
                                    n.inlTimes,
                                    a(n.inlTimes))
                                }
                                r.get({
                                    url: "/cgi-bin/loginauth?action=ask",
                                    timeout: 5e3
                                }, function(e) {
                                    1 === e.status ? (t.commit("__set_state", {
                                        state: "state_confirmed"
                                    }),
                                    t.dispatch("bizLogin", n)) : 2 === e.status ? t.commit("__set_state", {
                                        state: "state_cancel",
                                        step: 2
                                    }) : 3 === e.status ? t.commit("__set_state", {
                                        state: "state_timeout",
                                        step: 2
                                    }) : 4 === e.status || 0 === e.status ? o() : 0 !== e.status && t.commit("__set_state", {
                                        state: "state_failed",
                                        step: 2
                                    })
                                }, function() {
                                    o()
                                })
                            },
                            __set_state: function(e, t) {
                                e.commit("__set_state", t)
                            }
                        }
                    }
                }
            }),
            components: {
                "mp-faq-hover": b
            },
            data: function() {
                var e = navigator.userAgent
                  , t = !1;
                return (/(iPhone|iPod|iOS)/i.test(e) || /(Android)/i.test(e)) && (t = !0,
                v(284042, 0)),
                {
                    supportLang: [{
                        name: "简体中文",
                        value: "zh_CN"
                    }, {
                        name: "English",
                        value: "en_US"
                    }],
                    CgiData: o,
                    accountDom: null,
                    pwdDom: null,
                    verifyDom: null,
                    supportSafeInput: !1,
                    isShowQrcode: !1,
                    newKf: !1,
                    qqBindMailUrl: "",
                    showMpAppGuide: t
                }
            },
            created: function() {
                this.isStopQrcodeTimer = !1,
                this.qrcodeRefreshTimes = 0,
                this.qrcodeTimer = null,
                this.checkQrcodeTimes = 1,
                this.sessionid = +new Date + "" + Math.floor(100 * Math.random()),
                this.prepageState = null,
                this.hasStartLogin = !1
            },
            mounted: function() {
                var t = this;
                m().then(function(e) {
                    t.newKf = e
                }),
                this.accountDom = this.$refs.accountInput.$refs.field,
                this.verifyDom = this.$refs.verifyInput.$refs.field,
                this.supportSafeInput ? (this.pwdDom = x.domMap.password,
                this.pwdDom.addEventListener("input", function() {
                    t.$store.dispatch("__set_state", {
                        pwd: t.pwdDom.value.trim()
                    })
                }),
                this.pwdDom.addEventListener("keydown", function(e) {
                    13 === e.keyCode && t.login()
                }),
                u.remove("password_leak", {
                    path: "/"
                }),
                this.$refs.fakePwdInput.addEventListener("input", function() {
                    u.cookie("password_leak", location.href, {
                        path: "/"
                    })
                })) : this.pwdDom = this.$refs.pwdInput.$refs.field,
                u.cookie("remember_acct") && this.$store.commit("__set_state", {
                    rememberCheck: !0,
                    account: u.cookie("remember_acct")
                }),
                (this.$store.state.main.rememberCheck ? this.pwdDom : this.accountDom).focus(),
                this.$store.dispatch("getIngorePassList"),
                1 === this.mode && this.getQrcode(),
                localStorage.getItem("loginWithQrcode") && (this.switchMode(1),
                localStorage.removeItem("loginWithQrcode"))
            },
            computed: function(o) {
                for (var e = 1; e < arguments.length; e++) {
                    var r = null != arguments[e] ? arguments[e] : {};
                    e % 2 ? n(Object(r), !0).forEach(function(e) {
                        var t, n;
                        t = o,
                        n = r[e = e],
                        e in t ? Object.defineProperty(t, e, {
                            value: n,
                            enumerable: !0,
                            configurable: !0,
                            writable: !0
                        }) : t[e] = n
                    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(o, Object.getOwnPropertyDescriptors(r)) : n(Object(r)).forEach(function(e) {
                        Object.defineProperty(o, e, Object.getOwnPropertyDescriptor(r, e))
                    })
                }
                return o
            }({
                account: {
                    get: function() {
                        return this.$store.state.main.account
                    },
                    set: function(e) {
                        this.$store.dispatch("__set_state", {
                            account: e
                        })
                    }
                },
                pwd: {
                    get: function() {
                        return this.$store.state.main.pwd
                    },
                    set: function(e) {
                        this.$store.dispatch("__set_state", {
                            pwd: e
                        })
                    }
                },
                verify: {
                    get: function() {
                        return this.$store.state.main.verify
                    },
                    set: function(e) {
                        this.$store.dispatch("__set_state", {
                            verify: e
                        })
                    }
                },
                currentLang: {
                    get: function() {
                        return this.$store.state.main.currentLang
                    },
                    set: function(e) {
                        this.$store.dispatch("setLanguage", {
                            currentLang: e
                        })
                    }
                }
            }, g.mapState({
                step: function(e) {
                    return e.main.step
                },
                mode: function(e) {
                    return e.main.mode
                },
                qrcodeSrc: function(e) {
                    return e.main.qrcodeSrc
                },
                scanLoginType: function(e) {
                    return e.main.scanLoginType
                },
                err: function(e) {
                    return e.main.err
                },
                activeBizIndex: function(e) {
                    return e.main.activeBizIndex
                },
                verifyImg: function(e) {
                    return e.main.verifyImg
                },
                isNeedVerify: function(e) {
                    return e.main.isNeedVerify
                },
                rememberCheck: function(e) {
                    return e.main.rememberCheck
                },
                bizList: function(e) {
                    return e.main.bizList
                },
                state: function(e) {
                    return e.main.state
                },
                wxList: function(e) {
                    return e.main.wxList
                },
                activeWxIndex: function(e) {
                    return e.main.activeWxIndex
                },
                rejectWxList: function(e) {
                    return e.main.rejectWxList
                },
                currentLangDesc: function() {
                    for (var e = "简体中文", t = 0; t < this.supportLang.length; t++)
                        this.supportLang[t].value === this.currentLang && (e = this.supportLang[t].name);
                    return e
                }
            })),
            watch: {
                account: function(e) {
                    "" !== e && this.$store.dispatch("__set_state", {
                        err: ""
                    })
                },
                pwd: function(e) {
                    "" !== e && this.$store.dispatch("__set_state", {
                        err: ""
                    })
                },
                verify: function(e) {
                    !0 === this.$store.state.main.isNeedVerify && "" !== e && this.$store.dispatch("__set_state", {
                        err: ""
                    })
                },
                step: function(e) {
                    0 === e && (this.report19015({
                        optype: 1,
                        page_state: 1 === this.mode ? 3 : 1
                    }),
                    1 === this.mode && this.getQrcode())
                },
                mode: function(e) {
                    this.report19015({
                        optype: 1,
                        page_state: 1 === e ? 3 : 1
                    })
                }
            },
            methods: {
                report19015: function(e) {
                    1 === e.optype && (null !== this.prepageState && (e.prepage_state = this.prepageState),
                    this.prepageState = e.page_state),
                    h.report(19015, _({
                        devicetype: 1,
                        newsessionid: this.sessionid
                    }, e))
                },
                toggleQrcodeShow: function() {
                    this.isShowQrcode = !0
                },
                toggleQrcodeHide: function() {
                    this.isShowQrcode = !1
                },
                setLanguage: function(e) {
                    this.$store.dispatch("setLanguage", {
                        currentLang: e
                    })
                },
                switchMode: function(e) {
                    this.$store.commit("switchMode", {
                        mode: e
                    }),
                    1 === e ? (this.report19015({
                        optype: 2,
                        buttonid: 1
                    }),
                    this.getQrcode()) : (this.report19015({
                        optype: 2,
                        buttonid: 2
                    }),
                    this.refreshQrcode(),
                    this.stopCheckQrcode(),
                    this.hasStartLogin = !1)
                },
                switchScanLoginType: function(e) {
                    this.$store.commit("switchScanLoginType", {
                        scanLoginType: e
                    })
                },
                getQrcode: function() {
                    var n = this;
                    this.isStopQrcodeTimer = !1,
                    r.post({
                        url: "/cgi-bin/bizlogin?action=startlogin",
                        data: {
                            userlang: this.currentLang,
                            redirect_url: o.redirectUrl,
                            login_type: 3,
                            sessionid: this.sessionid
                        }
                    }, function(e) {
                        e && e.base_resp && 0 === e.base_resp.ret ? (n.hasStartLogin = !0,
                        n.isStopQrcodeTimer || n.refreshQrcode()) : (s.setSum(125091, 0, 2),
                        s.send(),
                        n.switchScanLoginType(6))
                    }, function(e, t) {
                        s.setSum(125091, 0, 3),
                        s.send(),
                        n.switchScanLoginType(6)
                    })
                },
                qrcodeError: function(e) {
                    e.target.src !== location.href && (s.setSum(125091, 1, 1),
                    s.send(),
                    this.stopCheckQrcode(),
                    this.switchScanLoginType(6))
                },
                refreshQrcode: function(e) {
                    "object" !== t(e) && e || (this.qrcodeRefreshTimes = 0),
                    this.stopCheckQrcode(),
                    5 <= this.qrcodeRefreshTimes ? this.switchScanLoginType(5) : (this.switchScanLoginType(0),
                    this.$store.commit("refreshQrcode"))
                },
                startCheckQrcode: function(e) {
                    e || (this.checkQrcodeTimes = 1),
                    this.qrcodeTimer = setTimeout(this.checkQrcode, a(this.checkQrcodeTimes))
                },
                stopCheckQrcode: function() {
                    this.isStopQrcodeTimer = !0,
                    this.qrcodeTimer && (clearTimeout(this.qrcodeTimer),
                    this.qrcodeTimer = null)
                },
                checkQrcode: function() {
                    var n = this;
                    r.get({
                        url: "/cgi-bin/scanloginqrcode?action=ask"
                    }, function(e) {
                        if (e && e.base_resp && 0 === e.base_resp.ret)
                            switch (e.status) {
                            case 1:
                                n.$store.dispatch("bizLogin", {
                                    currentLang: n.currentLang,
                                    loginType: 3
                                });
                                break;
                            case 2:
                                n.refreshQrcode();
                                break;
                            case 3:
                                n.refreshQrcode(!0);
                                break;
                            case 4:
                            case 6:
                                1 === e.acct_size ? n.switchScanLoginType(1) : 1 < e.acct_size ? n.switchScanLoginType(2) : n.switchScanLoginType(3),
                                n.startCheckQrcode(!0);
                                break;
                            case 5:
                                e.binduin ? (n.qqBindMailUrl = "/cgi-bin/bizunbindqq?action=page&qq=".concat(e.binduin),
                                n.switchScanLoginType(7)) : n.switchScanLoginType(4);
                                break;
                            default:
                                n.startCheckQrcode(!0)
                            }
                        else
                            n.switchScanLoginType(6)
                    }, function(e, t) {
                        n.startCheckQrcode(!0)
                    })
                },
                goRegist: function(e) {
                    this.report19015({
                        optype: 2,
                        buttonid: 3
                    }),
                    location.href = e.target.dataset.href
                },
                login: function() {
                    var e = this.$store.state.main.account
                      , t = this.$store.state.main.pwd
                      , n = this.$store.state.main.verify
                      , o = this.$store.state.main.isNeedVerify
                      , r = this.$store.state.main.currentLang
                      , i = +new Date;
                    "" === e ? (this.$store.dispatch("__set_state", {
                        err: "你还没有输入帐号！"
                    }),
                    this.accountDom.focus()) : "" === t ? (this.$store.dispatch("__set_state", {
                        err: "你还没有输入密码！"
                    }),
                    this.pwdDom.focus()) : !0 === o && "" === n ? (this.$store.dispatch("__set_state", {
                        err: "你还没有输入验证码！"
                    }),
                    this.verifyDom.focus()) : (0 === this.step && 0 === this.mode || (s.setSum(125091, 4, 1),
                    s.send()),
                    this.$store.dispatch("login", {
                        account: e,
                        pwd: t,
                        verify: n,
                        currentLang: r,
                        rand: i
                    }))
                },
                verifyImgRefresh: function() {
                    var e = +new Date
                      , t = this.$store.state.main.account;
                    this.$store.dispatch("verifyImgRefresh", {
                        account: t,
                        rand: e
                    })
                },
                selectBiz: function(e) {
                    this.$store.dispatch("__set_state", {
                        activeBizIndex: e
                    })
                },
                quickLogin1: function() {
                    this.$store.dispatch("quickLogin1")
                },
                changeToInputLogin: function() {
                    this.$store.dispatch("__set_state", {
                        step: 0
                    })
                },
                selectWx: function(e) {
                    "state_login" === this.$store.state.main.state || "state_confirmed" === this.$store.state.main.state || this.$store.state.main.rejectWxList[this.$store.state.main.activeBizIndex][e] || (1 < this.$store.state.main.wxList.length && this.$store.state.main.activeWxIndex === e ? this.$store.dispatch("__set_state", {
                        activeWxIndex: -1,
                        state: "state_waiting"
                    }) : this.$store.dispatch("__set_state", {
                        activeWxIndex: e,
                        state: "state_chosen"
                    }))
                },
                quickLogin2: function() {
                    "state_login" === this.$store.state.main.state || "state_confirmed" === this.$store.state.main.state || "state_reject" === this.$store.state.main.state || this.$store.state.main.rejectWxList[this.$store.state.main.activeBizIndex][this.$store.state.main.activeWxIndex] || this.$store.dispatch("quickLogin2", {
                        currentLang: this.currentLang
                    })
                },
                backToQuickLogin: function() {
                    "state_login" === this.$store.state.main.state && this.$store.dispatch("__set_state", {
                        state: "state_chosen"
                    }),
                    this.$store.dispatch("__set_state", {
                        step: this.$store.state.main.step - 1
                    })
                },
                changeRemember: function() {
                    this.$store.dispatch("__set_state", {
                        rememberCheck: !this.$store.state.main.rememberCheck
                    })
                },
                jump2DownloadMpApp: function() {
                    v(284042, 1);
                    var e = navigator.userAgent
                      , e = /(iPhone|iPod|iOS)/i.test(e);
                    location.href = e ? "https://itunes.apple.com/cn/app/订阅号助手/id1116013197?mt=8" : "https://a.app.qq.com/o/simple.jsp?pkgname=com.tencent.mp"
                }
            }
        });
        w.setBasicTime({
            pid: 30
        }),
        w.send(),
        window.vm = c,
        d.exports = c
    },
    "./src/pages/login/loginpage/style/loginpage.en_US.less": function(e, t, n) {},
    "./src/pages/login/loginpage/style/loginpage.less": function(e, t, n) {},
    "./src/pages/modules/safe_input/safe_input.js": function(e, t) {
        try {
            var n = new Function("\nlet id = 0;\nconst domMap = {};\nconst map = new WeakMap();\ncustomElements.define('mp-safe-input', class extends HTMLElement {\n  constructor() {\n    super();\n    map.set(this, {\n      id: id++,\n      root: this.attachShadow({ mode: 'closed' })\n    });\n  }\n  connectedCallback() {\n    const style = document.createElement('style');\n    const input = document.createElement('input');\n    const attrs = this.attributes;\n    for (let i = 0; i < attrs.length; i++) {\n      if (attrs[i].name === 'input-style') {\n        style.innerHTML += 'input{' + attrs[i].value + '}';\n      } else if (attrs[i].name === 'placeholder-style') {\n        style.innerHTML += 'input::placeholder{' + attrs[i].value + '}';\n      } else if (['class', 'style'].indexOf(attrs[i].name) === -1) {\n        input.setAttribute(attrs[i].name, attrs[i].value);\n      }\n    }\n    const inst = map.get(this);\n    inst.root.appendChild(style);\n    inst.root.appendChild(input);\n    const name = this.getAttribute('name') || inst.id;\n    domMap[name] = input;\n  }\n});\nreturn {\n  domMap: domMap,\n  support: true\n};\n")()
        } catch (e) {
            Math.random() < .005 && window.WX_BJ_REPORT && window.WX_BJ_REPORT.BadJs && "function" == typeof window.WX_BJ_REPORT.BadJs.onError && (e.name = "SafeInput:" + e.name,
            window.WX_BJ_REPORT.BadJs.onError(e)),
            n = {
                domMap: {},
                support: !1
            }
        }
        e.exports = n
    },
    "./src/pages/modules/utils/get_cgi_data.js": function(e, t) {
        e.exports = function(e) {
            return window.CGI_DATA[e]
        }
    },
    34: function(e, t, n) {
        e.exports = n("./src/pages/login/loginpage/loginpage.js")
    }
});
