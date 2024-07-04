/* @preserve
 * Leaflet 1.5.1, a JS library for interactive maps. http://leafletjs.com
 * (c) 2010-2018 Vladimir Agafonkin, (c) 2010-2011 CloudMade
 */
(function(n, t)
{
    typeof exports == "object" && typeof module != "undefined" ? t(exports) : typeof define == "function" && define.amd ? define(["exports"], t) : t(n.L = {})
})(this, function(n)
{
    "use strict";
    function s(n)
    {
        for (var i, r, t = 1, u = arguments.length; t < u; t++)
        {
            r = arguments[t];
            for (i in r)
                n[i] = r[i]
        }
        return n
    }
    function c(n, t)
    {
        var i = Array.prototype.slice,
            r;
        return n.bind ? n.bind.apply(n, i.call(arguments, 1)) : (r = i.call(arguments, 2), function()
            {
                return n.apply(t, r.length ? r.concat(i.call(arguments)) : arguments)
            })
    }
    function o(n)
    {
        return n._leaflet_id = n._leaflet_id || ++lf, n._leaflet_id
    }
    function af(n, t, i)
    {
        var u,
            r,
            f,
            e;
        return e = function()
            {
                u = !1;
                r && (f.apply(i, r), r = !1)
            }, f = function()
            {
                u ? r = arguments : (n.apply(i, arguments), setTimeout(e, t), u = !0)
            }
    }
    function ar(n, t, i)
    {
        var f = t[1],
            r = t[0],
            u = f - r;
        return n === f && i ? n : ((n - r) % u + u) % u + r
    }
    function k()
    {
        return !1
    }
    function yt(n, t)
    {
        return t = t === undefined ? 6 : t, +(Math.round(n + ("e+" + t)) + ("e-" + t))
    }
    function vf(n)
    {
        return n.trim ? n.trim() : n.replace(/^\s+|\s+$/g, "")
    }
    function pi(n)
    {
        return vf(n).split(/\s+/)
    }
    function l(n, t)
    {
        n.hasOwnProperty("options") || (n.options = n.options ? lr(n.options) : {});
        for (var i in t)
            n.options[i] = t[i];
        return n.options
    }
    function os(n, t, i)
    {
        var u = [];
        for (var r in n)
            u.push(encodeURIComponent(i ? r.toUpperCase() : r) + "=" + encodeURIComponent(n[r]));
        return (!t || t.indexOf("?") === -1 ? "?" : "&") + u.join("&")
    }
    function hs(n, t)
    {
        return n.replace(ss, function(n, i)
            {
                var r = t[i];
                if (r === undefined)
                    throw new Error("No value provided for variable " + n);
                else
                    typeof r == "function" && (r = r(t));
                return r
            })
    }
    function cs(n, t)
    {
        for (var i = 0; i < n.length; i++)
            if (n[i] === t)
                return i;
        return -1
    }
    function yf(n)
    {
        return window["webkit" + n] || window["moz" + n] || window["ms" + n]
    }
    function ls(n)
    {
        var t = +new Date,
            i = Math.max(0, 16 - (t - pf));
        return pf = t + i, window.setTimeout(n, i)
    }
    function g(n, t, i)
    {
        if (i && su === ls)
            n.call(t);
        else
            return su.call(window, c(n, t))
    }
    function nt(n)
    {
        n && wf.call(window, n)
    }
    function gt(){}
    function pc(n)
    {
        if (typeof L != "undefined" && L && L.Mixin)
        {
            n = ht(n) ? n : [n];
            for (var t = 0; t < n.length; t++)
                n[t] === L.Mixin.Events && console.warn("Deprecated include of L.Mixin.Events: this property will be removed in future releases, please inherit from L.Evented instead.", (new Error).stack)
        }
    }
    function t(n, t, i)
    {
        this.x = i ? Math.round(n) : n;
        this.y = i ? Math.round(t) : t
    }
    function r(n, i, r)
    {
        return n instanceof t ? n : ht(n) ? new t(n[0], n[1]) : n === undefined || n === null ? n : typeof n == "object" && "x" in n && "y" in n ? new t(n.x, n.y) : new t(n, i, r)
    }
    function a(n, t)
    {
        var r,
            i,
            u;
        if (n)
            for (r = t ? [n, t] : n, i = 0, u = r.length; i < u; i++)
                this.extend(r[i])
    }
    function ct(n, t)
    {
        return !n || n instanceof a ? n : new a(n, t)
    }
    function it(n, t)
    {
        var r,
            i,
            u;
        if (n)
            for (r = t ? [n, t] : n, i = 0, u = r.length; i < u; i++)
                this.extend(r[i])
    }
    function d(n, t)
    {
        return n instanceof it ? n : new it(n, t)
    }
    function h(n, t, i)
    {
        if (isNaN(n) || isNaN(t))
            throw new Error("Invalid LatLng object: (" + n + ", " + t + ")");
        this.lat = +n;
        this.lng = +t;
        i !== undefined && (this.alt = +i)
    }
    function y(n, t, i)
    {
        return n instanceof h ? n : ht(n) && typeof n[0] != "object" ? n.length === 3 ? new h(n[0], n[1], n[2]) : n.length === 2 ? new h(n[0], n[1]) : null : n === undefined || n === null ? n : typeof n == "object" && "lat" in n ? new h(n.lat, "lng" in n ? n.lng : n.lon, n.alt) : t === undefined ? null : new h(n, t, i)
    }
    function df(n, t, i, r)
    {
        if (ht(n))
        {
            this._a = n[0];
            this._b = n[1];
            this._c = n[2];
            this._d = n[3];
            return
        }
        this._a = n;
        this._b = t;
        this._c = i;
        this._d = r
    }
    function yr(n, t, i, r)
    {
        return new df(n, t, i, r)
    }
    function ps(n)
    {
        return document.createElementNS("http://www.w3.org/2000/svg", n)
    }
    function ws(n, t)
    {
        for (var u = "", i, s, f, e, r = 0, o = n.length; r < o; r++)
        {
            for (f = n[r], i = 0, s = f.length; i < s; i++)
                e = f[i],
                u += (i ? "L" : "M") + e.x + " " + e.y;
            u += t ? lu ? "z" : "x" : ""
        }
        return u || "M0 0"
    }
    function wt(n)
    {
        return navigator.userAgent.toLowerCase().indexOf(n) >= 0
    }
    function tl(n, t, i, r)
    {
        return t === "touchstart" ? rl(n, i, r) : t === "touchmove" ? el(n, i, r) : t === "touchend" && ol(n, i, r), this
    }
    function il(n, t, i)
    {
        var r = n["_leaflet_" + t + i];
        return t === "touchstart" ? n.removeEventListener(fe, r, !1) : t === "touchmove" ? n.removeEventListener(ee, r, !1) : t === "touchend" && (n.removeEventListener(oe, r, !1), n.removeEventListener(se, r, !1)), this
    }
    function rl(n, t, i)
    {
        var r = c(function(n)
            {
                if (n.pointerType !== "mouse" && n.MSPOINTER_TYPE_MOUSE && n.pointerType !== n.MSPOINTER_TYPE_MOUSE)
                    if (nl.indexOf(n.target.tagName) < 0)
                        et(n);
                    else
                        return;
                ce(n, t)
            });
        n["_leaflet_touchstart" + i] = r;
        n.addEventListener(fe, r, !1);
        uh || (document.documentElement.addEventListener(fe, ul, !0), document.documentElement.addEventListener(ee, fl, !0), document.documentElement.addEventListener(oe, fh, !0), document.documentElement.addEventListener(se, fh, !0), uh = !0)
    }
    function ul(n)
    {
        gi[n.pointerId] = n;
        he++
    }
    function fl(n)
    {
        gi[n.pointerId] && (gi[n.pointerId] = n)
    }
    function fh(n)
    {
        delete gi[n.pointerId];
        he--
    }
    function ce(n, t)
    {
        n.touches = [];
        for (var i in gi)
            n.touches.push(gi[i]);
        n.changedTouches = [n];
        t(n)
    }
    function el(n, t, i)
    {
        var r = function(n)
            {
                (n.pointerType !== n.MSPOINTER_TYPE_MOUSE && n.pointerType !== "mouse" || n.buttons !== 0) && ce(n, t)
            };
        n["_leaflet_touchmove" + i] = r;
        n.addEventListener(ee, r, !1)
    }
    function ol(n, t, i)
    {
        var r = function(n)
            {
                ce(n, t)
            };
        n["_leaflet_touchend" + i] = r;
        n.addEventListener(oe, r, !1);
        n.addEventListener(se, r, !1)
    }
    function eh(n, t, i)
    {
        function e(n)
        {
            var i,
                t,
                e;
            if (lt)
            {
                if (!pr || n.pointerType === "mouse")
                    return;
                i = he
            }
            else
                i = n.touches.length;
            i > 1 || (t = Date.now(), e = t - (u || t), r = n.touches ? n.touches[0] : n, f = e > 0 && e <= s, u = t)
        }
        function o(n)
        {
            if (f && !r.cancelBubble)
            {
                if (lt)
                {
                    if (!pr || n.pointerType === "mouse")
                        return;
                    var e = {},
                        i;
                    for (var o in r)
                        i = r[o],
                        e[o] = i && i.bind ? i.bind(r) : i;
                    r = e
                }
                r.type = "dblclick";
                r.button = 0;
                t(r);
                u = null
            }
        }
        var u,
            r,
            f = !1,
            s = 250;
        return n[nr + vu + i] = e, n[nr + yu + i] = o, n[nr + "dblclick" + i] = t, n.addEventListener(vu, e, !1), n.addEventListener(yu, o, !1), n.addEventListener("dblclick", t, !1), this
    }
    function oh(n, t)
    {
        var i = n[nr + vu + t],
            r = n[nr + yu + t],
            u = n[nr + "dblclick" + t];
        return n.removeEventListener(vu, i, !1), n.removeEventListener(yu, r, !1), pr || n.removeEventListener("dblclick", u, !1), this
    }
    function hh(n)
    {
        return typeof n == "string" ? document.getElementById(n) : n
    }
    function dr(n, t)
    {
        var i = n.style[t] || n.currentStyle && n.currentStyle[t],
            r;
        return (!i || i === "auto") && document.defaultView && (r = document.defaultView.getComputedStyle(n, null), i = r ? r[t] : null), i === "auto" ? null : i
    }
    function e(n, t, i)
    {
        var r = document.createElement(n);
        return r.className = t || "", i && i.appendChild(r), r
    }
    function v(n)
    {
        var t = n.parentNode;
        t && t.removeChild(n)
    }
    function pu(n)
    {
        while (n.firstChild)
            n.removeChild(n.firstChild)
    }
    function tr(n)
    {
        var t = n.parentNode;
        t && t.lastChild !== n && t.appendChild(n)
    }
    function ir(n)
    {
        var t = n.parentNode;
        t && t.firstChild !== n && t.insertBefore(n, t.firstChild)
    }
    function ae(n, t)
    {
        if (n.classList !== undefined)
            return n.classList.contains(t);
        var i = wu(n);
        return i.length > 0 && new RegExp("(^|\\s)" + t + "(\\s|$)").test(i)
    }
    function i(n, t)
    {
        var r,
            i,
            f,
            u;
        if (n.classList !== undefined)
            for (r = pi(t), i = 0, f = r.length; i < f; i++)
                n.classList.add(r[i]);
        else
            ae(n, t) || (u = wu(n), ve(n, (u ? u + " " : "") + t))
    }
    function p(n, t)
    {
        n.classList !== undefined ? n.classList.remove(t) : ve(n, vf((" " + wu(n) + " ").replace(" " + t + " ", " ")))
    }
    function ve(n, t)
    {
        n.className.baseVal === undefined ? n.className = t : n.className.baseVal = t
    }
    function wu(n)
    {
        return n.correspondingElement && (n = n.correspondingElement), n.className.baseVal === undefined ? n.className : n.className.baseVal
    }
    function ut(n, t)
    {
        "opacity" in n.style ? n.style.opacity = t : "filter" in n.style && sl(n, t)
    }
    function sl(n, t)
    {
        var i = !1,
            r = "DXImageTransform.Microsoft.Alpha";
        try
        {
            i = n.filters.item(r)
        }
        catch(u)
        {
            if (t === 1)
                return
        }
        t = Math.round(t * 100);
        i ? (i.Enabled = t !== 100, i.Opacity = t) : n.style.filter += " progid:" + r + "(opacity=" + t + ")"
    }
    function bu(n)
    {
        for (var i = document.documentElement.style, t = 0; t < n.length; t++)
            if (n[t] in i)
                return n[t];
        return !1
    }
    function si(n, i, r)
    {
        var u = i || new t(0, 0);
        n.style[le] = (re ? "translate(" + u.x + "px," + u.y + "px)" : "translate3d(" + u.x + "px," + u.y + "px,0)") + (r ? " scale(" + r + ")" : "")
    }
    function b(n, t)
    {
        n._leaflet_pos = t;
        rt ? si(n, t) : (n.style.left = t.x + "px", n.style.top = t.y + "px")
    }
    function oi(n)
    {
        return n._leaflet_pos || new t(0, 0)
    }
    function pe()
    {
        u(window, "dragstart", et)
    }
    function we()
    {
        w(window, "dragstart", et)
    }
    function ke(n)
    {
        while (n.tabIndex === -1)
            n = n.parentNode;
        n.style && (du(), ku = n, be = n.style.outline, n.style.outline = "none", u(window, "keydown", du))
    }
    function du()
    {
        ku && (ku.style.outline = be, ku = undefined, be = undefined, w(window, "keydown", du))
    }
    function ch(n)
    {
        do
            n = n.parentNode;
        while ((!n.offsetWidth || !n.offsetHeight) && n !== document.body);
        return n
    }
    function de(n)
    {
        var t = n.getBoundingClientRect();
        return {
                x: t.width / n.offsetWidth || 1, y: t.height / n.offsetHeight || 1, boundingClientRect: t
            }
    }
    function u(n, t, i, r)
    {
        var f,
            u,
            e;
        if (typeof t == "object")
            for (f in t)
                gu(n, f, t[f], i);
        else
            for (t = pi(t), u = 0, e = t.length; u < e; u++)
                gu(n, t[u], i, r);
        return this
    }
    function w(n, t, i, r)
    {
        var f,
            u,
            o,
            e;
        if (typeof t == "object")
            for (f in t)
                ge(n, f, t[f], i);
        else if (t)
            for (t = pi(t), u = 0, o = t.length; u < o; u++)
                ge(n, t[u], i, r);
        else
        {
            for (e in n[ft])
                ge(n, e, n[ft][e]);
            delete n[ft]
        }
        return this
    }
    function gu(n, t, i, r)
    {
        var f = t + o(i) + (r ? "_" + o(r) : ""),
            u,
            e;
        if (n[ft] && n[ft][f])
            return this;
        u = function(t)
        {
            return i.call(r || n, t || window.event)
        };
        e = u;
        lt && t.indexOf("touch") === 0 ? tl(n, t, u, f) : !pt || t !== "dblclick" || !eh || lt && br ? "addEventListener" in n ? t === "mousewheel" ? n.addEventListener("onwheel" in n ? "wheel" : "mousewheel", u, !1) : t === "mouseenter" || t === "mouseleave" ? (u = function(t)
        {
            t = t || window.event;
            tf(n, t) && e(t)
        }, n.addEventListener(t === "mouseenter" ? "mouseover" : "mouseout", u, !1)) : (t === "click" && ki && (u = function(n)
        {
            hl(n, e)
        }), n.addEventListener(t, u, !1)) : "attachEvent" in n && n.attachEvent("on" + t, u) : eh(n, u, f);
        n[ft] = n[ft] || {};
        n[ft][f] = u
    }
    function ge(n, t, i, r)
    {
        var u = t + o(i) + (r ? "_" + o(r) : ""),
            f = n[ft] && n[ft][u];
        if (!f)
            return this;
        lt && t.indexOf("touch") === 0 ? il(n, t, u) : !pt || t !== "dblclick" || !oh || lt && br ? "removeEventListener" in n ? t === "mousewheel" ? n.removeEventListener("onwheel" in n ? "wheel" : "mousewheel", f, !1) : n.removeEventListener(t === "mouseenter" ? "mouseover" : t === "mouseleave" ? "mouseout" : t, f, !1) : "detachEvent" in n && n.detachEvent("on" + t, f) : oh(n, u);
        n[ft][u] = null
    }
    function hi(n)
    {
        return n.stopPropagation ? n.stopPropagation() : n.originalEvent ? n.originalEvent._stopped = !0 : n.cancelBubble = !0, io(n), this
    }
    function no(n)
    {
        return gu(n, "mousewheel", hi), this
    }
    function tu(n)
    {
        return u(n, "mousedown touchstart dblclick", hi), gu(n, "click", to), this
    }
    function et(n)
    {
        return n.preventDefault ? n.preventDefault() : n.returnValue = !1, this
    }
    function bt(n)
    {
        return et(n), hi(n), this
    }
    function ah(n, i)
    {
        if (!i)
            return new t(n.clientX, n.clientY);
        var r = de(i),
            u = r.boundingClientRect;
        return new t((n.clientX - u.left) / r.x - i.clientLeft, (n.clientY - u.top) / r.y - i.clientTop)
    }
    function yh(n)
    {
        return pr ? n.wheelDeltaY / 2 : n.deltaY && n.deltaMode === 0 ? -n.deltaY / vh : n.deltaY && n.deltaMode === 1 ? -n.deltaY * 20 : n.deltaY && n.deltaMode === 2 ? -n.deltaY * 60 : n.deltaX || n.deltaZ ? 0 : n.wheelDelta ? (n.wheelDeltaY || n.wheelDelta) / 2 : n.detail && Math.abs(n.detail) < 32765 ? -n.detail * 20 : n.detail ? n.detail / -32765 * 60 : 0
    }
    function to(n)
    {
        nf[n.type] = !0
    }
    function io(n)
    {
        var t = nf[n.type];
        return nf[n.type] = !1, t
    }
    function tf(n, t)
    {
        var i = t.relatedTarget;
        if (!i)
            return !0;
        try
        {
            while (i && i !== n)
                i = i.parentNode
        }
        catch(r)
        {
            return !1
        }
        return i !== n
    }
    function hl(n, t)
    {
        var r = n.timeStamp || n.originalEvent && n.originalEvent.timeStamp,
            i = ro && r - ro;
        if (i && i > 100 && i < 500 || n.target._simulatedClick && !n._simulated)
        {
            bt(n);
            return
        }
        ro = r;
        t(n)
    }
    function ll(n, t)
    {
        return new f(n, t)
    }
    function nc(n, t)
    {
        if (!t || !n.length)
            return n.slice();
        var i = t * t;
        return n = kl(n, i), bl(n, i)
    }
    function tc(n, t, i)
    {
        return Math.sqrt(iu(n, t, i, !0))
    }
    function wl(n, t, i)
    {
        return iu(n, t, i)
    }
    function bl(n, t)
    {
        var r = n.length,
            e = typeof Uint8Array != undefined + "" ? Uint8Array : Array,
            u = new e(r),
            i,
            f;
        for (u[0] = u[r - 1] = 1, oo(n, u, t, 0, r - 1), f = [], i = 0; i < r; i++)
            u[i] && f.push(n[i]);
        return f
    }
    function oo(n, t, i, r, u)
    {
        for (var o = 0, e, s, f = r + 1; f <= u - 1; f++)
            s = iu(n[f], n[r], n[u], !0),
            s > o && (e = f, o = s);
        o > i && (t[e] = 1, oo(n, t, i, r, e), oo(n, t, i, e, u))
    }
    function kl(n, t)
    {
        for (var r = [n[0]], i = 1, u = 0, f = n.length; i < f; i++)
            dl(n[i], n[u]) > t && (r.push(n[i]), u = i);
        return u < f - 1 && r.push(n[f - 1]), r
    }
    function rc(n, t, i, r, u)
    {
        var f = r ? ic : li(n, i),
            e = li(t, i),
            s,
            o,
            h;
        for (ic = e; ; )
        {
            if (!(f | e))
                return [n, t];
            if (f & e)
                return !1;
            s = f || e;
            o = rf(n, t, s, i, u);
            h = li(o, i);
            s === f ? (n = o, f = h) : (t = o, e = h)
        }
    }
    function rf(n, i, r, u, f)
    {
        var s = i.x - n.x,
            h = i.y - n.y,
            c = u.min,
            l = u.max,
            e,
            o;
        return r & 8 ? (e = n.x + s * (l.y - n.y) / h, o = l.y) : r & 4 ? (e = n.x + s * (c.y - n.y) / h, o = c.y) : r & 2 ? (e = l.x, o = n.y + h * (l.x - n.x) / s) : r & 1 && (e = c.x, o = n.y + h * (c.x - n.x) / s), new t(e, o, f)
    }
    function li(n, t)
    {
        var i = 0;
        return n.x < t.min.x ? i |= 1 : n.x > t.max.x && (i |= 2), n.y < t.min.y ? i |= 4 : n.y > t.max.y && (i |= 8), i
    }
    function dl(n, t)
    {
        var i = t.x - n.x,
            r = t.y - n.y;
        return i * i + r * r
    }
    function iu(n, i, r, u)
    {
        var o = i.x,
            s = i.y,
            f = r.x - o,
            e = r.y - s,
            c = f * f + e * e,
            h;
        return c > 0 && (h = ((n.x - o) * f + (n.y - s) * e) / c, h > 1 ? (o = r.x, s = r.y) : h > 0 && (o += f * h, s += e * h)), f = n.x - o, e = n.y - s, u ? f * f + e * e : new t(o, s)
    }
    function ti(n)
    {
        return !ht(n[0]) || typeof n[0][0] != "object" && typeof n[0][0] != "undefined"
    }
    function uc(n)
    {
        return console.warn("Deprecated use of _flat, please use L.LineUtil.isFlat instead."), ti(n)
    }
    function ec(n, t, i)
    {
        for (var e, a = [1, 4, 2, 8], l, c, o, s, f, u, r = 0, h = n.length; r < h; r++)
            n[r]._code = li(n[r], t);
        for (c = 0; c < 4; c++)
        {
            for (f = a[c], e = [], r = 0, h = n.length, l = h - 1; r < h; l = r++)
                o = n[r],
                s = n[l],
                o._code & f ? s._code & f || (u = rf(s, o, f, t, i), u._code = li(u, t), e.push(u)) : (s._code & f && (u = rf(s, o, f, t, i), u._code = li(u, t), e.push(u)), e.push(o));
            n = e
        }
        return n
    }
    function fa(n)
    {
        return new or(n)
    }
    function ea(n, t)
    {
        return new uu(n, t)
    }
    function oa(n, t)
    {
        return new fu(n, t)
    }
    function sa(n, t, i)
    {
        return new uf(n, t, i)
    }
    function ha(n, t)
    {
        return new kt(n, t)
    }
    function ca(n, t)
    {
        return new ai(n, t)
    }
    function lo(n, t)
    {
        var i = n.type === "Feature" ? n.geometry : n,
            u = i ? i.coordinates : null,
            e = [],
            o = t && t.pointToLayer,
            s = t && t.coordsToLatLng || ao,
            f,
            h,
            r,
            c,
            l;
        if (!u && !i)
            return null;
        switch (i.type)
        {
            case"Point":
                return f = s(u), o ? o(n, f) : new uu(f);
            case"MultiPoint":
                for (r = 0, c = u.length; r < c; r++)
                    f = s(u[r]),
                    e.push(o ? o(n, f) : new uu(f));
                return new er(e);
            case"LineString":
            case"MultiLineString":
                return h = ff(u, i.type === "LineString" ? 0 : 1, s), new kt(h, t);
            case"Polygon":
            case"MultiPolygon":
                return h = ff(u, i.type === "Polygon" ? 1 : 2, s), new ai(h, t);
            case"GeometryCollection":
                for (r = 0, c = i.geometries.length; r < c; r++)
                    l = lo({
                        geometry: i.geometries[r], type: "Feature", properties: n.properties
                    }, t),
                    l && e.push(l);
                return new er(e);
            default:
                throw new Error("Invalid GeoJSON object.");
        }
    }
    function ao(n)
    {
        return new h(n[1], n[0], n[2])
    }
    function ff(n, t, i)
    {
        for (var u = [], r = 0, e = n.length, f; r < e; r++)
            f = t ? ff(n[r], t - 1, i) : (i || ao)(n[r]),
            u.push(f);
        return u
    }
    function vo(n, t)
    {
        return t = typeof t == "number" ? t : 6, n.alt !== undefined ? [yt(n.lng, t), yt(n.lat, t), yt(n.alt, t)] : [yt(n.lng, t), yt(n.lat, t)]
    }
    function ef(n, t, i, r)
    {
        for (var u = [], f = 0, e = n.length; f < e; f++)
            u.push(t ? ef(n[f], t - 1, i, r) : vo(n[f], r));
        return !t && i && u.push(u[0]), u
    }
    function sr(n, t)
    {
        return n.feature ? s({}, n.feature, {geometry: t}) : of(t)
    }
    function of(n)
    {
        return n.type === "Feature" || n.type === "FeatureCollection" ? n : {
                type: "Feature", properties: {}, geometry: n
            }
    }
    function sc(n, t)
    {
        return new dt(n, t)
    }
    function va(n, t, i)
    {
        return new hc(n, t, i)
    }
    function ya(n, t, i)
    {
        return new yo(n, t, i)
    }
    function wa(n)
    {
        return new po(n)
    }
    function ba(n)
    {
        return new cr(n)
    }
    function lc(n, t)
    {
        return new yi(n, t)
    }
    function ka(n, t)
    {
        return new wo(n, t)
    }
    function ac(n)
    {
        return rh ? new bo(n) : null
    }
    function vc(n)
    {
        return lu || au ? new ou(n) : null
    }
    function ga(n, t)
    {
        return new ko(n, t)
    }
    var es = Object.freeze,
        lr,
        lf,
        ss,
        ht,
        vr,
        pf,
        su,
        wf,
        as,
        tt,
        wi,
        bf,
        hu,
        ys,
        gr,
        nu,
        ye,
        rr,
        ku,
        be,
        lh,
        ft,
        vh,
        nf,
        ro,
        ot,
        ur,
        kh,
        at,
        ic,
        fc,
        st,
        ii,
        fu,
        uf,
        kt,
        ai,
        dt,
        sf,
        yo,
        vi,
        cc,
        po,
        cr,
        yi,
        wo,
        vt,
        bo,
        ko,
        go,
        ns,
        ts,
        is,
        rs,
        us,
        fs,
        yc;
    Object.freeze = function(n)
    {
        return n
    };
    lr = Object.create || function()
    {
        function n(){}
        return function(t)
            {
                return n.prototype = t, new n
            }
    }();
    lf = 0;
    ss = /\{ *([\w_-]+) *\}/g;
    ht = Array.isArray || function(n)
    {
        return Object.prototype.toString.call(n) === "[object Array]"
    };
    vr = "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=";
    pf = 0;
    su = window.requestAnimationFrame || yf("RequestAnimationFrame") || ls;
    wf = window.cancelAnimationFrame || yf("CancelAnimationFrame") || yf("CancelRequestAnimationFrame") || function(n)
    {
        window.clearTimeout(n)
    };
    as = (Object.freeze || Object)({
        freeze: es, extend: s, create: lr, bind: c, lastId: lf, stamp: o, throttle: af, wrapNum: ar, falseFn: k, formatNum: yt, trim: vf, splitWords: pi, setOptions: l, getParamString: os, template: hs, isArray: ht, indexOf: cs, emptyImageUrl: vr, requestFn: su, cancelFn: wf, requestAnimFrame: g, cancelAnimFrame: nt
    });
    gt.extend = function(n)
    {
        var i = function()
            {
                this.initialize && this.initialize.apply(this, arguments);
                this.callInitHooks()
            },
            u = i.__super__ = this.prototype,
            t = lr(u),
            r;
        t.constructor = i;
        i.prototype = t;
        for (r in this)
            this.hasOwnProperty(r) && r !== "prototype" && r !== "__super__" && (i[r] = this[r]);
        return n.statics && (s(i, n.statics), delete n.statics), n.includes && (pc(n.includes), s.apply(null, [t].concat(n.includes)), delete n.includes), t.options && (n.options = s(lr(t.options), n.options)), s(t, n), t._initHooks = [], t.callInitHooks = function()
                {
                    if (!this._initHooksCalled)
                    {
                        u.callInitHooks && u.callInitHooks.call(this);
                        this._initHooksCalled = !0;
                        for (var n = 0, i = t._initHooks.length; n < i; n++)
                            t._initHooks[n].call(this)
                    }
                }, i
    };
    gt.include = function(n)
    {
        return s(this.prototype, n), this
    };
    gt.mergeOptions = function(n)
    {
        return s(this.prototype.options, n), this
    };
    gt.addInitHook = function(n)
    {
        var t = Array.prototype.slice.call(arguments, 1),
            i = typeof n == "function" ? n : function()
            {
                this[n].apply(this, t)
            };
        return this.prototype._initHooks = this.prototype._initHooks || [], this.prototype._initHooks.push(i), this
    };
    tt = {
        on: function(n, t, i)
        {
            var u,
                r,
                f;
            if (typeof n == "object")
                for (u in n)
                    this._on(u, n[u], t);
            else
                for (n = pi(n), r = 0, f = n.length; r < f; r++)
                    this._on(n[r], t, i);
            return this
        }, off: function(n, t, i)
            {
                var u,
                    r,
                    f;
                if (n)
                    if (typeof n == "object")
                        for (u in n)
                            this._off(u, n[u], t);
                    else
                        for (n = pi(n), r = 0, f = n.length; r < f; r++)
                            this._off(n[r], t, i);
                else
                    delete this._events;
                return this
            }, _on: function(n, t, i)
            {
                var r,
                    e,
                    u,
                    f,
                    o;
                for (this._events = this._events || {}, r = this._events[n], r || (r = [], this._events[n] = r), i === this && (i = undefined), e = {
                        fn: t, ctx: i
                    }, u = r, f = 0, o = u.length; f < o; f++)
                    if (u[f].fn === t && u[f].ctx === i)
                        return;
                u.push(e)
            }, _off: function(n, t, i)
            {
                var r,
                    u,
                    f,
                    e;
                if (this._events && (r = this._events[n], r))
                {
                    if (!t)
                    {
                        for (u = 0, f = r.length; u < f; u++)
                            r[u].fn = k;
                        delete this._events[n];
                        return
                    }
                    if (i === this && (i = undefined), r)
                        for (u = 0, f = r.length; u < f; u++)
                            if ((e = r[u], e.ctx === i) && e.fn === t)
                            {
                                e.fn = k;
                                this._firingCount && (this._events[n] = r = r.slice());
                                r.splice(u, 1);
                                return
                            }
                }
            }, fire: function(n, t, i)
            {
                var f,
                    r,
                    u,
                    o,
                    e;
                if (!this.listens(n, i))
                    return this;
                if (f = s({}, t, {
                    type: n, target: this, sourceTarget: t && t.sourceTarget || this
                }), this._events && (r = this._events[n], r))
                {
                    for (this._firingCount = this._firingCount + 1 || 1, u = 0, o = r.length; u < o; u++)
                        e = r[u],
                        e.fn.call(e.ctx || this, f);
                    this._firingCount--
                }
                return i && this._propagateEvent(f), this
            }, listens: function(n, t)
            {
                var i = this._events && this._events[n],
                    r;
                if (i && i.length)
                    return !0;
                if (t)
                    for (r in this._eventParents)
                        if (this._eventParents[r].listens(n, t))
                            return !0;
                return !1
            }, once: function(n, t, i)
            {
                var r,
                    u;
                if (typeof n == "object")
                {
                    for (r in n)
                        this.once(r, n[r], t);
                    return this
                }
                u = c(function()
                {
                    this.off(n, t, i).off(n, u, i)
                }, this);
                return this.on(n, t, i).on(n, u, i)
            }, addEventParent: function(n)
            {
                return this._eventParents = this._eventParents || {}, this._eventParents[o(n)] = n, this
            }, removeEventParent: function(n)
            {
                return this._eventParents && delete this._eventParents[o(n)], this
            }, _propagateEvent: function(n)
            {
                for (var t in this._eventParents)
                    this._eventParents[t].fire(n.type, s({
                        layer: n.target, propagatedFrom: n.target
                    }, n), !0)
            }
    };
    tt.addEventListener = tt.on;
    tt.removeEventListener = tt.clearAllEventListeners = tt.off;
    tt.addOneTimeEventListener = tt.once;
    tt.fireEvent = tt.fire;
    tt.hasEventListeners = tt.listens;
    wi = gt.extend(tt);
    bf = Math.trunc || function(n)
    {
        return n > 0 ? Math.floor(n) : Math.ceil(n)
    };
    t.prototype = {
        clone: function()
        {
            return new t(this.x, this.y)
        }, add: function(n)
            {
                return this.clone()._add(r(n))
            }, _add: function(n)
            {
                return this.x += n.x, this.y += n.y, this
            }, subtract: function(n)
            {
                return this.clone()._subtract(r(n))
            }, _subtract: function(n)
            {
                return this.x -= n.x, this.y -= n.y, this
            }, divideBy: function(n)
            {
                return this.clone()._divideBy(n)
            }, _divideBy: function(n)
            {
                return this.x /= n, this.y /= n, this
            }, multiplyBy: function(n)
            {
                return this.clone()._multiplyBy(n)
            }, _multiplyBy: function(n)
            {
                return this.x *= n, this.y *= n, this
            }, scaleBy: function(n)
            {
                return new t(this.x * n.x, this.y * n.y)
            }, unscaleBy: function(n)
            {
                return new t(this.x / n.x, this.y / n.y)
            }, round: function()
            {
                return this.clone()._round()
            }, _round: function()
            {
                return this.x = Math.round(this.x), this.y = Math.round(this.y), this
            }, floor: function()
            {
                return this.clone()._floor()
            }, _floor: function()
            {
                return this.x = Math.floor(this.x), this.y = Math.floor(this.y), this
            }, ceil: function()
            {
                return this.clone()._ceil()
            }, _ceil: function()
            {
                return this.x = Math.ceil(this.x), this.y = Math.ceil(this.y), this
            }, trunc: function()
            {
                return this.clone()._trunc()
            }, _trunc: function()
            {
                return this.x = bf(this.x), this.y = bf(this.y), this
            }, distanceTo: function(n)
            {
                n = r(n);
                var t = n.x - this.x,
                    i = n.y - this.y;
                return Math.sqrt(t * t + i * i)
            }, equals: function(n)
            {
                return n = r(n), n.x === this.x && n.y === this.y
            }, contains: function(n)
            {
                return n = r(n), Math.abs(n.x) <= Math.abs(this.x) && Math.abs(n.y) <= Math.abs(this.y)
            }, toString: function()
            {
                return "Point(" + yt(this.x) + ", " + yt(this.y) + ")"
            }
    };
    a.prototype = {
        extend: function(n)
        {
            return n = r(n), this.min || this.max ? (this.min.x = Math.min(n.x, this.min.x), this.max.x = Math.max(n.x, this.max.x), this.min.y = Math.min(n.y, this.min.y), this.max.y = Math.max(n.y, this.max.y)) : (this.min = n.clone(), this.max = n.clone()), this
        }, getCenter: function(n)
            {
                return new t((this.min.x + this.max.x) / 2, (this.min.y + this.max.y) / 2, n)
            }, getBottomLeft: function()
            {
                return new t(this.min.x, this.max.y)
            }, getTopRight: function()
            {
                return new t(this.max.x, this.min.y)
            }, getTopLeft: function()
            {
                return this.min
            }, getBottomRight: function()
            {
                return this.max
            }, getSize: function()
            {
                return this.max.subtract(this.min)
            }, contains: function(n)
            {
                var i,
                    u;
                return n = typeof n[0] == "number" || n instanceof t ? r(n) : ct(n), n instanceof a ? (i = n.min, u = n.max) : i = u = n, i.x >= this.min.x && u.x <= this.max.x && i.y >= this.min.y && u.y <= this.max.y
            }, intersects: function(n)
            {
                n = ct(n);
                var t = this.min,
                    i = this.max,
                    r = n.min,
                    u = n.max,
                    f = u.x >= t.x && r.x <= i.x,
                    e = u.y >= t.y && r.y <= i.y;
                return f && e
            }, overlaps: function(n)
            {
                n = ct(n);
                var t = this.min,
                    i = this.max,
                    r = n.min,
                    u = n.max,
                    f = u.x > t.x && r.x < i.x,
                    e = u.y > t.y && r.y < i.y;
                return f && e
            }, isValid: function()
            {
                return !!(this.min && this.max)
            }
    };
    it.prototype = {
        extend: function(n)
        {
            var r = this._southWest,
                u = this._northEast,
                t,
                i;
            if (n instanceof h)
                t = n,
                i = n;
            else if (n instanceof it)
            {
                if (t = n._southWest, i = n._northEast, !t || !i)
                    return this
            }
            else
                return n ? this.extend(y(n) || d(n)) : this;
            return r || u ? (r.lat = Math.min(t.lat, r.lat), r.lng = Math.min(t.lng, r.lng), u.lat = Math.max(i.lat, u.lat), u.lng = Math.max(i.lng, u.lng)) : (this._southWest = new h(t.lat, t.lng), this._northEast = new h(i.lat, i.lng)), this
        }, pad: function(n)
            {
                var t = this._southWest,
                    i = this._northEast,
                    r = Math.abs(t.lat - i.lat) * n,
                    u = Math.abs(t.lng - i.lng) * n;
                return new it(new h(t.lat - r, t.lng - u), new h(i.lat + r, i.lng + u))
            }, getCenter: function()
            {
                return new h((this._southWest.lat + this._northEast.lat) / 2, (this._southWest.lng + this._northEast.lng) / 2)
            }, getSouthWest: function()
            {
                return this._southWest
            }, getNorthEast: function()
            {
                return this._northEast
            }, getNorthWest: function()
            {
                return new h(this.getNorth(), this.getWest())
            }, getSouthEast: function()
            {
                return new h(this.getSouth(), this.getEast())
            }, getWest: function()
            {
                return this._southWest.lng
            }, getSouth: function()
            {
                return this._southWest.lat
            }, getEast: function()
            {
                return this._northEast.lng
            }, getNorth: function()
            {
                return this._northEast.lat
            }, contains: function(n)
            {
                n = typeof n[0] == "number" || n instanceof h || "lat" in n ? y(n) : d(n);
                var r = this._southWest,
                    u = this._northEast,
                    t,
                    i;
                return n instanceof it ? (t = n.getSouthWest(), i = n.getNorthEast()) : t = i = n, t.lat >= r.lat && i.lat <= u.lat && t.lng >= r.lng && i.lng <= u.lng
            }, intersects: function(n)
            {
                n = d(n);
                var t = this._southWest,
                    i = this._northEast,
                    r = n.getSouthWest(),
                    u = n.getNorthEast(),
                    f = u.lat >= t.lat && r.lat <= i.lat,
                    e = u.lng >= t.lng && r.lng <= i.lng;
                return f && e
            }, overlaps: function(n)
            {
                n = d(n);
                var t = this._southWest,
                    i = this._northEast,
                    r = n.getSouthWest(),
                    u = n.getNorthEast(),
                    f = u.lat > t.lat && r.lat < i.lat,
                    e = u.lng > t.lng && r.lng < i.lng;
                return f && e
            }, toBBoxString: function()
            {
                return [this.getWest(), this.getSouth(), this.getEast(), this.getNorth()].join(",")
            }, equals: function(n, t)
            {
                return n ? (n = d(n), this._southWest.equals(n.getSouthWest(), t) && this._northEast.equals(n.getNorthEast(), t)) : !1
            }, isValid: function()
            {
                return !!(this._southWest && this._northEast)
            }
    };
    h.prototype = {
        equals: function(n, t)
        {
            if (!n)
                return !1;
            n = y(n);
            var i = Math.max(Math.abs(this.lat - n.lat), Math.abs(this.lng - n.lng));
            return i <= (t === undefined ? 1e-9 : t)
        }, toString: function(n)
            {
                return "LatLng(" + yt(this.lat, n) + ", " + yt(this.lng, n) + ")"
            }, distanceTo: function(n)
            {
                return ui.distance(this, y(n))
            }, wrap: function()
            {
                return ui.wrapLatLng(this)
            }, toBounds: function(n)
            {
                var t = 180 * n / 40075017,
                    i = t / Math.cos(Math.PI / 180 * this.lat);
                return d([this.lat - t, this.lng - i], [this.lat + t, this.lng + i])
            }, clone: function()
            {
                return new h(this.lat, this.lng, this.alt)
            }
    };
    var ni = {
            latLngToPoint: function(n, t)
            {
                var i = this.projection.project(n),
                    r = this.scale(t);
                return this.transformation._transform(i, r)
            }, pointToLatLng: function(n, t)
                {
                    var i = this.scale(t),
                        r = this.transformation.untransform(n, i);
                    return this.projection.unproject(r)
                }, project: function(n)
                {
                    return this.projection.project(n)
                }, unproject: function(n)
                {
                    return this.projection.unproject(n)
                }, scale: function(n)
                {
                    return 256 * Math.pow(2, n)
                }, zoom: function(n)
                {
                    return Math.log(n / 256) / Math.LN2
                }, getProjectedBounds: function(n)
                {
                    if (this.infinite)
                        return null;
                    var t = this.projection.bounds,
                        i = this.scale(n),
                        r = this.transformation.transform(t.min, i),
                        u = this.transformation.transform(t.max, i);
                    return new a(r, u)
                }, infinite: !1, wrapLatLng: function(n)
                {
                    var t = this.wrapLng ? ar(n.lng, this.wrapLng, !0) : n.lng,
                        i = this.wrapLat ? ar(n.lat, this.wrapLat, !0) : n.lat,
                        r = n.alt;
                    return new h(i, t, r)
                }, wrapLatLngBounds: function(n)
                {
                    var t = n.getCenter(),
                        u = this.wrapLatLng(t),
                        i = t.lat - u.lat,
                        r = t.lng - u.lng;
                    if (i === 0 && r === 0)
                        return n;
                    var f = n.getSouthWest(),
                        e = n.getNorthEast(),
                        o = new h(f.lat - i, f.lng - r),
                        s = new h(e.lat - i, e.lng - r);
                    return new it(o, s)
                }
        },
        ui = s({}, ni, {
            wrapLng: [-180, 180], R: 6371e3, distance: function(n, t)
                {
                    var i = Math.PI / 180,
                        e = n.lat * i,
                        o = t.lat * i,
                        r = Math.sin((t.lat - n.lat) * i / 2),
                        u = Math.sin((t.lng - n.lng) * i / 2),
                        f = r * r + Math.cos(e) * Math.cos(o) * u * u,
                        s = 2 * Math.atan2(Math.sqrt(f), Math.sqrt(1 - f));
                    return this.R * s
                }
        }),
        vs = 6378137,
        kf = {
            R: vs, MAX_LATITUDE: 85.0511287798, project: function(n)
                {
                    var i = Math.PI / 180,
                        r = this.MAX_LATITUDE,
                        f = Math.max(Math.min(r, n.lat), -r),
                        u = Math.sin(f * i);
                    return new t(this.R * n.lng * i, this.R * Math.log((1 + u) / (1 - u)) / 2)
                }, unproject: function(n)
                {
                    var t = 180 / Math.PI;
                    return new h((2 * Math.atan(Math.exp(n.y / this.R)) - Math.PI / 2) * t, n.x * t / this.R)
                }, bounds: function()
                {
                    var n = vs * Math.PI;
                    return new a([-n, -n], [n, n])
                }()
        };
    df.prototype = {
        transform: function(n, t)
        {
            return this._transform(n.clone(), t)
        }, _transform: function(n, t)
            {
                return t = t || 1, n.x = t * (this._a * n.x + this._b), n.y = t * (this._c * n.y + this._d), n
            }, untransform: function(n, i)
            {
                return i = i || 1, new t((n.x / i - this._b) / this._a, (n.y / i - this._d) / this._c)
            }
    };
    hu = s({}, ui, {
        code: "EPSG:3857", projection: kf, transformation: function()
            {
                var n = .5 / (Math.PI * kf.R);
                return yr(n, .5, -n, .5)
            }()
    });
    ys = s({}, hu, {code: "EPSG:900913"});
    var gf = document.documentElement.style,
        cu = "ActiveXObject" in window,
        bi = cu && !document.addEventListener,
        pr = "msLaunchUri" in navigator && !("documentMode" in document),
        ne = wt("webkit"),
        ki = wt("android"),
        wr = wt("android 2") || wt("android 3"),
        wc = parseInt(/WebKit\/([0-9]+)|$/.exec(navigator.userAgent)[1], 10),
        bs = ki && wt("Google") && wc < 537 && !("AudioNode" in window),
        te = !!window.opera,
        br = wt("chrome"),
        ie = wt("gecko") && !ne && !te && !cu,
        ks = !br && wt("safari"),
        ds = wt("phantom"),
        gs = "OTransition" in gf,
        nh = navigator.platform.indexOf("Win") === 0,
        re = cu && "transition" in gf,
        ue = "WebKitCSSMatrix" in window && "m11" in new window.WebKitCSSMatrix && !wr,
        th = "MozPerspective" in gf,
        rt = !window.L_DISABLE_3D && (re || ue || th) && !gs && !ds,
        di = typeof orientation != "undefined" || wt("mobile"),
        bc = di && ne,
        kc = di && ue,
        fi = !window.PointerEvent && window.MSPointerEvent,
        lt = !!(window.PointerEvent || fi),
        pt = !window.L_NO_TOUCH && (lt || "ontouchstart" in window || window.DocumentTouch && document instanceof window.DocumentTouch),
        ih = di && te,
        dc = di && ie,
        ei = (window.devicePixelRatio || window.screen.deviceXDPI / window.screen.logicalXDPI) > 1,
        rh = function()
        {
            return !!document.createElement("canvas").getContext
        }(),
        lu = !!(document.createElementNS && ps("svg").createSVGRect),
        au = !lu && function()
        {
            var t,
                n;
            try
            {
                return t = document.createElement("div"), t.innerHTML = '<v:shape adj="1"/>', n = t.firstChild, n.style.behavior = "url(#default#VML)", n && typeof n.adj == "object"
            }
            catch(i)
            {
                return !1
            }
        }();
    var gc = (Object.freeze || Object)({
            ie: cu, ielt9: bi, edge: pr, webkit: ne, android: ki, android23: wr, androidStock: bs, opera: te, chrome: br, gecko: ie, safari: ks, phantom: ds, opera12: gs, win: nh, ie3d: re, webkit3d: ue, gecko3d: th, any3d: rt, mobile: di, mobileWebkit: bc, mobileWebkit3d: kc, msPointer: fi, pointer: lt, touch: pt, mobileOpera: ih, mobileGecko: dc, retina: ei, canvas: rh, svg: lu, vml: au
        }),
        fe = fi ? "MSPointerDown" : "pointerdown",
        ee = fi ? "MSPointerMove" : "pointermove",
        oe = fi ? "MSPointerUp" : "pointerup",
        se = fi ? "MSPointerCancel" : "pointercancel",
        nl = ["INPUT", "SELECT", "OPTION"],
        gi = {},
        uh = !1,
        he = 0;
    var vu = fi ? "MSPointerDown" : lt ? "pointerdown" : "touchstart",
        yu = fi ? "MSPointerUp" : lt ? "pointerup" : "touchend",
        nr = "_leaflet_";
    var le = bu(["transform", "webkitTransform", "OTransform", "MozTransform", "msTransform"]),
        kr = bu(["webkitTransition", "transition", "OTransition", "MozTransition", "msTransition"]),
        sh = kr === "webkitTransition" || kr === "OTransition" ? kr + "End" : "transitionend";
    "onselectstart" in document ? (gr = function()
    {
        u(window, "selectstart", et)
    }, nu = function()
    {
        w(window, "selectstart", et)
    }) : (rr = bu(["userSelect", "WebkitUserSelect", "OUserSelect", "MozUserSelect", "msUserSelect"]), gr = function()
    {
        if (rr)
        {
            var n = document.documentElement.style;
            ye = n[rr];
            n[rr] = "none"
        }
    }, nu = function()
        {
            rr && (document.documentElement.style[rr] = ye, ye = undefined)
        });
    lh = (Object.freeze || Object)({
        TRANSFORM: le, TRANSITION: kr, TRANSITION_END: sh, get: hh, getStyle: dr, create: e, remove: v, empty: pu, toFront: tr, toBack: ir, hasClass: ae, addClass: i, removeClass: p, setClass: ve, getClass: wu, setOpacity: ut, testProp: bu, setTransform: si, setPosition: b, getPosition: oi, disableTextSelection: gr, enableTextSelection: nu, disableImageDrag: pe, enableImageDrag: we, preventOutline: ke, restoreOutline: du, getSizedParentNode: ch, getScale: de
    });
    ft = "_leaflet_events";
    vh = nh && br ? 2 * window.devicePixelRatio : ie ? window.devicePixelRatio : 1;
    nf = {};
    var cl = (Object.freeze || Object)({
            on: u, off: w, stopPropagation: hi, disableScrollPropagation: no, disableClickPropagation: tu, preventDefault: et, stop: bt, getMousePosition: ah, getWheelDelta: yh, fakeStop: to, skipped: io, isExternalTarget: tf, addListener: u, removeListener: w
        }),
        ph = wi.extend({
            run: function(n, t, i, r)
            {
                this.stop();
                this._el = n;
                this._inProgress = !0;
                this._duration = i || .25;
                this._easeOutPower = 1 / Math.max(r || .5, .2);
                this._startPos = oi(n);
                this._offset = t.subtract(this._startPos);
                this._startTime = +new Date;
                this.fire("start");
                this._animate()
            }, stop: function()
                {
                    this._inProgress && (this._step(!0), this._complete())
                }, _animate: function()
                {
                    this._animId = g(this._animate, this);
                    this._step()
                }, _step: function(n)
                {
                    var t = +new Date - this._startTime,
                        i = this._duration * 1e3;
                    t < i ? this._runFrame(this._easeOut(t / i), n) : (this._runFrame(1), this._complete())
                }, _runFrame: function(n, t)
                {
                    var i = this._startPos.add(this._offset.multiplyBy(n));
                    t && i._round();
                    b(this._el, i);
                    this.fire("step")
                }, _complete: function()
                {
                    nt(this._animId);
                    this._inProgress = !1;
                    this.fire("end")
                }, _easeOut: function(n)
                {
                    return 1 - Math.pow(1 - n, this._easeOutPower)
                }
        }),
        f = wi.extend({
            options: {
                crs: hu, center: undefined, zoom: undefined, minZoom: undefined, maxZoom: undefined, layers: [], maxBounds: undefined, renderer: undefined, zoomAnimation: !0, zoomAnimationThreshold: 4, fadeAnimation: !0, markerZoomAnimation: !0, transform3DLimit: 8388608, zoomSnap: 1, zoomDelta: 1, trackResize: !0
            }, initialize: function(n, t)
                {
                    t = l(this, t);
                    this._handlers = [];
                    this._layers = {};
                    this._zoomBoundLayers = {};
                    this._sizeChanged = !0;
                    this._initContainer(n);
                    this._initLayout();
                    this._onResize = c(this._onResize, this);
                    this._initEvents();
                    t.maxBounds && this.setMaxBounds(t.maxBounds);
                    t.zoom !== undefined && (this._zoom = this._limitZoom(t.zoom));
                    t.center && t.zoom !== undefined && this.setView(y(t.center), t.zoom, {reset: !0});
                    this.callInitHooks();
                    this._zoomAnimated = kr && rt && !ih && this.options.zoomAnimation;
                    this._zoomAnimated && (this._createAnimProxy(), u(this._proxy, sh, this._catchTransitionEnd, this));
                    this._addLayers(this.options.layers)
                }, setView: function(n, t, i)
                {
                    if (t = t === undefined ? this._zoom : this._limitZoom(t), n = this._limitCenter(y(n), t, this.options.maxBounds), i = i || {}, this._stop(), this._loaded && !i.reset && i !== !0)
                    {
                        i.animate !== undefined && (i.zoom = s({animate: i.animate}, i.zoom), i.pan = s({
                            animate: i.animate, duration: i.duration
                        }, i.pan));
                        var r = this._zoom !== t ? this._tryAnimatedZoom && this._tryAnimatedZoom(n, t, i.zoom) : this._tryAnimatedPan(n, i.pan);
                        if (r)
                            return clearTimeout(this._sizeTimer), this
                    }
                    return this._resetView(n, t), this
                }, setZoom: function(n, t)
                {
                    return this._loaded ? this.setView(this.getCenter(), n, {zoom: t}) : (this._zoom = n, this)
                }, zoomIn: function(n, t)
                {
                    return n = n || (rt ? this.options.zoomDelta : 1), this.setZoom(this._zoom + n, t)
                }, zoomOut: function(n, t)
                {
                    return n = n || (rt ? this.options.zoomDelta : 1), this.setZoom(this._zoom - n, t)
                }, setZoomAround: function(n, i, r)
                {
                    var f = this.getZoomScale(i),
                        u = this.getSize().divideBy(2),
                        e = n instanceof t ? n : this.latLngToContainerPoint(n),
                        o = e.subtract(u).multiplyBy(1 - 1 / f),
                        s = this.containerPointToLatLng(u.add(o));
                    return this.setView(s, i, {zoom: r})
                }, _getBoundsCenterZoom: function(n, t)
                {
                    t = t || {};
                    n = n.getBounds ? n.getBounds() : d(n);
                    var u = r(t.paddingTopLeft || t.padding || [0, 0]),
                        f = r(t.paddingBottomRight || t.padding || [0, 0]),
                        i = this.getBoundsZoom(n, !1, u.add(f));
                    if (i = typeof t.maxZoom == "number" ? Math.min(t.maxZoom, i) : i, i === Infinity)
                        return {
                                center: n.getCenter(), zoom: i
                            };
                    var e = f.subtract(u).divideBy(2),
                        o = this.project(n.getSouthWest(), i),
                        s = this.project(n.getNorthEast(), i),
                        h = this.unproject(o.add(s).divideBy(2).add(e), i);
                    return {
                            center: h, zoom: i
                        }
                }, fitBounds: function(n, t)
                {
                    if (n = d(n), !n.isValid())
                        throw new Error("Bounds are not valid.");
                    var i = this._getBoundsCenterZoom(n, t);
                    return this.setView(i.center, i.zoom, t)
                }, fitWorld: function(n)
                {
                    return this.fitBounds([[-90, -180], [90, 180]], n)
                }, panTo: function(n, t)
                {
                    return this.setView(n, this._zoom, {pan: t})
                }, panBy: function(n, t)
                {
                    if (n = r(n).round(), t = t || {}, !n.x && !n.y)
                        return this.fire("moveend");
                    if (t.animate !== !0 && !this.getSize().contains(n))
                        return this._resetView(this.unproject(this.project(this.getCenter()).add(n)), this.getZoom()), this;
                    if (!this._panAnim)
                    {
                        this._panAnim = new ph;
                        this._panAnim.on({
                            step: this._onPanTransitionStep, end: this._onPanTransitionEnd
                        }, this)
                    }
                    if (t.noMoveStart || this.fire("movestart"), t.animate !== !1)
                    {
                        i(this._mapPane, "leaflet-pan-anim");
                        var u = this._getMapPanePos().subtract(n).round();
                        this._panAnim.run(this._mapPane, u, t.duration || .25, t.easeLinearity)
                    }
                    else
                        this._rawPanBy(n),
                        this.fire("move").fire("moveend");
                    return this
                }, flyTo: function(n, t, i)
                {
                    function p(n)
                    {
                        var u = n ? -1 : 1,
                            f = n ? l : r,
                            e = l * l - r * r + u * s * s * o * o,
                            h = 2 * f * s * o,
                            t = e / h,
                            i = Math.sqrt(t * t + 1) - t;
                        return i < 1e-9 ? -18 : Math.log(i)
                    }
                    function w(n)
                    {
                        return (Math.exp(n) - Math.exp(-n)) / 2
                    }
                    function h(n)
                    {
                        return (Math.exp(n) + Math.exp(-n)) / 2
                    }
                    function d(n)
                    {
                        return w(n) / h(n)
                    }
                    function nt(n)
                    {
                        return r * (h(u) / h(u + f * n))
                    }
                    function tt(n)
                    {
                        return r * (h(u) * d(u + f * n) - w(u)) / s
                    }
                    function it(n)
                    {
                        return 1 - Math.pow(1 - n, 1.5)
                    }
                    function k()
                    {
                        var i = (Date.now() - ut) / ft,
                            u = it(i) * b;
                        i <= 1 ? (this._flyToFrame = g(k, this), this._move(this.unproject(c.add(a.subtract(c).multiplyBy(tt(u) / o)), e), this.getScaleZoom(r / nt(u), e), {flyTo: !0})) : this._move(n, t)._moveEnd(!0)
                    }
                    var u;
                    if (i = i || {}, i.animate === !1 || !rt)
                        return this.setView(n, t, i);
                    this._stop();
                    var c = this.project(this.getCenter()),
                        a = this.project(n),
                        v = this.getSize(),
                        e = this._zoom;
                    n = y(n);
                    t = t === undefined ? e : t;
                    var r = Math.max(v.x, v.y),
                        l = r * this.getZoomScale(e, t),
                        o = a.distanceTo(c) || 1,
                        f = 1.42,
                        s = f * f;
                    u = p(0);
                    var ut = Date.now(),
                        b = (p(1) - u) / f,
                        ft = i.duration ? 1e3 * i.duration : 1e3 * b * .8;
                    return this._moveStart(!0, i.noMoveStart), k.call(this), this
                }, flyToBounds: function(n, t)
                {
                    var i = this._getBoundsCenterZoom(n, t);
                    return this.flyTo(i.center, i.zoom, t)
                }, setMaxBounds: function(n)
                {
                    if (n = d(n), n.isValid())
                        this.options.maxBounds && this.off("moveend", this._panInsideMaxBounds);
                    else
                        return this.options.maxBounds = null, this.off("moveend", this._panInsideMaxBounds);
                    this.options.maxBounds = n;
                    this._loaded && this._panInsideMaxBounds();
                    return this.on("moveend", this._panInsideMaxBounds)
                }, setMinZoom: function(n)
                {
                    var t = this.options.minZoom;
                    return (this.options.minZoom = n, this._loaded && t !== n && (this.fire("zoomlevelschange"), this.getZoom() < this.options.minZoom)) ? this.setZoom(n) : this
                }, setMaxZoom: function(n)
                {
                    var t = this.options.maxZoom;
                    return (this.options.maxZoom = n, this._loaded && t !== n && (this.fire("zoomlevelschange"), this.getZoom() > this.options.maxZoom)) ? this.setZoom(n) : this
                }, panInsideBounds: function(n, t)
                {
                    this._enforcingBounds = !0;
                    var i = this.getCenter(),
                        r = this._limitCenter(i, this._zoom, d(n));
                    return i.equals(r) || this.panTo(r, t), this._enforcingBounds = !1, this
                }, panInside: function(n, t)
                {
                    var f,
                        u;
                    t = t || {};
                    var s = r(t.paddingTopLeft || t.padding || [0, 0]),
                        h = r(t.paddingBottomRight || t.padding || [0, 0]),
                        a = this.getCenter(),
                        c = this.project(a),
                        i = this.project(n),
                        l = this.getPixelBounds(),
                        o = l.getSize().divideBy(2),
                        e = ct([l.min.add(s), l.max.subtract(h)]);
                    return e.contains(i) || (this._enforcingBounds = !0, f = c.subtract(i), u = r(i.x + f.x, i.y + f.y), (i.x < e.min.x || i.x > e.max.x) && (u.x = c.x - f.x, f.x > 0 ? u.x += o.x - s.x : u.x -= o.x - h.x), (i.y < e.min.y || i.y > e.max.y) && (u.y = c.y - f.y, f.y > 0 ? u.y += o.y - s.y : u.y -= o.y - h.y), this.panTo(this.unproject(u), t), this._enforcingBounds = !1), this
                }, invalidateSize: function(n)
                {
                    var i;
                    if (!this._loaded)
                        return this;
                    n = s({
                        animate: !1, pan: !0
                    }, n === !0 ? {animate: !0} : n);
                    i = this.getSize();
                    this._sizeChanged = !0;
                    this._lastCenter = null;
                    var r = this.getSize(),
                        u = i.divideBy(2).round(),
                        f = r.divideBy(2).round(),
                        t = u.subtract(f);
                    return !t.x && !t.y ? this : (n.animate && n.pan ? this.panBy(t) : (n.pan && this._rawPanBy(t), this.fire("move"), n.debounceMoveend ? (clearTimeout(this._sizeTimer), this._sizeTimer = setTimeout(c(this.fire, this, "moveend"), 200)) : this.fire("moveend")), this.fire("resize", {
                            oldSize: i, newSize: r
                        }))
                }, stop: function()
                {
                    return this.setZoom(this._limitZoom(this._zoom)), this.options.zoomSnap || this.fire("viewreset"), this._stop()
                }, locate: function(n)
                {
                    if (n = this._locateOptions = s({
                        timeout: 1e4, watch: !1
                    }, n), !("geolocation" in navigator))
                        return this._handleGeolocationError({
                                code: 0, message: "Geolocation not supported."
                            }), this;
                    var t = c(this._handleGeolocationResponse, this),
                        i = c(this._handleGeolocationError, this);
                    return n.watch ? this._locationWatchId = navigator.geolocation.watchPosition(t, i, n) : navigator.geolocation.getCurrentPosition(t, i, n), this
                }, stopLocate: function()
                {
                    return navigator.geolocation && navigator.geolocation.clearWatch && navigator.geolocation.clearWatch(this._locationWatchId), this._locateOptions && (this._locateOptions.setView = !1), this
                }, _handleGeolocationError: function(n)
                {
                    var t = n.code,
                        i = n.message || (t === 1 ? "permission denied" : t === 2 ? "position unavailable" : "timeout");
                    this._locateOptions.setView && !this._loaded && this.fitWorld();
                    this.fire("locationerror", {
                        code: t, message: "Geolocation error: " + i + "."
                    })
                }, _handleGeolocationResponse: function(n)
                {
                    var o = n.coords.latitude,
                        s = n.coords.longitude,
                        i = new h(o, s),
                        e = i.toBounds(n.coords.accuracy * 2),
                        r = this._locateOptions,
                        u,
                        f,
                        t;
                    r.setView && (u = this.getBoundsZoom(e), this.setView(i, r.maxZoom ? Math.min(u, r.maxZoom) : u));
                    f = {
                        latlng: i, bounds: e, timestamp: n.timestamp
                    };
                    for (t in n.coords)
                        typeof n.coords[t] == "number" && (f[t] = n.coords[t]);
                    this.fire("locationfound", f)
                }, addHandler: function(n, t)
                {
                    if (!t)
                        return this;
                    var i = this[n] = new t(this);
                    return this._handlers.push(i), this.options[n] && i.enable(), this
                }, remove: function()
                {
                    if (this._initEvents(!0), this._containerId !== this._container._leaflet_id)
                        throw new Error("Map container is being reused by another instance");
                    try
                    {
                        delete this._container._leaflet_id;
                        delete this._containerId
                    }
                    catch(t)
                    {
                        this._container._leaflet_id = undefined;
                        this._containerId = undefined
                    }
                    this._locationWatchId !== undefined && this.stopLocate();
                    this._stop();
                    v(this._mapPane);
                    this._clearControlPos && this._clearControlPos();
                    this._resizeRequest && (nt(this._resizeRequest), this._resizeRequest = null);
                    this._clearHandlers();
                    this._loaded && this.fire("unload");
                    for (var n in this._layers)
                        this._layers[n].remove();
                    for (n in this._panes)
                        v(this._panes[n]);
                    return this._layers = [], this._panes = [], delete this._mapPane, delete this._renderer, this
                }, createPane: function(n, t)
                {
                    var r = "leaflet-pane" + (n ? " leaflet-" + n.replace("Pane", "") + "-pane" : ""),
                        i = e("div", r, t || this._mapPane);
                    return n && (this._panes[n] = i), i
                }, getCenter: function()
                {
                    return (this._checkIfLoaded(), this._lastCenter && !this._moved()) ? this._lastCenter : this.layerPointToLatLng(this._getCenterLayerPoint())
                }, getZoom: function()
                {
                    return this._zoom
                }, getBounds: function()
                {
                    var n = this.getPixelBounds(),
                        t = this.unproject(n.getBottomLeft()),
                        i = this.unproject(n.getTopRight());
                    return new it(t, i)
                }, getMinZoom: function()
                {
                    return this.options.minZoom === undefined ? this._layersMinZoom || 0 : this.options.minZoom
                }, getMaxZoom: function()
                {
                    return this.options.maxZoom === undefined ? this._layersMaxZoom === undefined ? Infinity : this._layersMaxZoom : this.options.maxZoom
                }, getBoundsZoom: function(n, t, i)
                {
                    n = d(n);
                    i = r(i || [0, 0]);
                    var u = this.getZoom() || 0,
                        c = this.getMinZoom(),
                        l = this.getMaxZoom(),
                        a = n.getNorthWest(),
                        v = n.getSouthEast(),
                        e = this.getSize().subtract(i),
                        o = ct(this.project(v, u), this.project(a, u)).getSize(),
                        f = rt ? this.options.zoomSnap : 1,
                        s = e.x / o.x,
                        h = e.y / o.y,
                        y = t ? Math.max(s, h) : Math.min(s, h);
                    return u = this.getScaleZoom(y, u), f && (u = Math.round(u / (f / 100)) * (f / 100), u = t ? Math.ceil(u / f) * f : Math.floor(u / f) * f), Math.max(c, Math.min(l, u))
                }, getSize: function()
                {
                    return (!this._size || this._sizeChanged) && (this._size = new t(this._container.clientWidth || 0, this._container.clientHeight || 0), this._sizeChanged = !1), this._size.clone()
                }, getPixelBounds: function(n, t)
                {
                    var i = this._getTopLeftPoint(n, t);
                    return new a(i, i.add(this.getSize()))
                }, getPixelOrigin: function()
                {
                    return this._checkIfLoaded(), this._pixelOrigin
                }, getPixelWorldBounds: function(n)
                {
                    return this.options.crs.getProjectedBounds(n === undefined ? this.getZoom() : n)
                }, getPane: function(n)
                {
                    return typeof n == "string" ? this._panes[n] : n
                }, getPanes: function()
                {
                    return this._panes
                }, getContainer: function()
                {
                    return this._container
                }, getZoomScale: function(n, t)
                {
                    var i = this.options.crs;
                    return t = t === undefined ? this._zoom : t, i.scale(n) / i.scale(t)
                }, getScaleZoom: function(n, t)
                {
                    var r = this.options.crs,
                        i;
                    return t = t === undefined ? this._zoom : t, i = r.zoom(n * r.scale(t)), isNaN(i) ? Infinity : i
                }, project: function(n, t)
                {
                    return t = t === undefined ? this._zoom : t, this.options.crs.latLngToPoint(y(n), t)
                }, unproject: function(n, t)
                {
                    return t = t === undefined ? this._zoom : t, this.options.crs.pointToLatLng(r(n), t)
                }, layerPointToLatLng: function(n)
                {
                    var t = r(n).add(this.getPixelOrigin());
                    return this.unproject(t)
                }, latLngToLayerPoint: function(n)
                {
                    var t = this.project(y(n))._round();
                    return t._subtract(this.getPixelOrigin())
                }, wrapLatLng: function(n)
                {
                    return this.options.crs.wrapLatLng(y(n))
                }, wrapLatLngBounds: function(n)
                {
                    return this.options.crs.wrapLatLngBounds(d(n))
                }, distance: function(n, t)
                {
                    return this.options.crs.distance(y(n), y(t))
                }, containerPointToLayerPoint: function(n)
                {
                    return r(n).subtract(this._getMapPanePos())
                }, layerPointToContainerPoint: function(n)
                {
                    return r(n).add(this._getMapPanePos())
                }, containerPointToLatLng: function(n)
                {
                    var t = this.containerPointToLayerPoint(r(n));
                    return this.layerPointToLatLng(t)
                }, latLngToContainerPoint: function(n)
                {
                    return this.layerPointToContainerPoint(this.latLngToLayerPoint(y(n)))
                }, mouseEventToContainerPoint: function(n)
                {
                    return ah(n, this._container)
                }, mouseEventToLayerPoint: function(n)
                {
                    return this.containerPointToLayerPoint(this.mouseEventToContainerPoint(n))
                }, mouseEventToLatLng: function(n)
                {
                    return this.layerPointToLatLng(this.mouseEventToLayerPoint(n))
                }, _initContainer: function(n)
                {
                    var t = this._container = hh(n);
                    if (t)
                    {
                        if (t._leaflet_id)
                            throw new Error("Map container is already initialized.");
                    }
                    else
                        throw new Error("Map container not found.");
                    u(t, "scroll", this._onScroll, this);
                    this._containerId = o(t)
                }, _initLayout: function()
                {
                    var t = this._container,
                        n;
                    this._fadeAnimated = this.options.fadeAnimation && rt;
                    i(t, "leaflet-container" + (pt ? " leaflet-touch" : "") + (ei ? " leaflet-retina" : "") + (bi ? " leaflet-oldie" : "") + (ks ? " leaflet-safari" : "") + (this._fadeAnimated ? " leaflet-fade-anim" : ""));
                    n = dr(t, "position");
                    n !== "absolute" && n !== "relative" && n !== "fixed" && (t.style.position = "relative");
                    this._initPanes();
                    this._initControlPos && this._initControlPos()
                }, _initPanes: function()
                {
                    var n = this._panes = {};
                    this._paneRenderers = {};
                    this._mapPane = this.createPane("mapPane", this._container);
                    b(this._mapPane, new t(0, 0));
                    this.createPane("tilePane");
                    this.createPane("shadowPane");
                    this.createPane("overlayPane");
                    this.createPane("markerPane");
                    this.createPane("tooltipPane");
                    this.createPane("popupPane");
                    this.options.markerZoomAnimation || (i(n.markerPane, "leaflet-zoom-hide"), i(n.shadowPane, "leaflet-zoom-hide"))
                }, _resetView: function(n, i)
                {
                    var u,
                        r;
                    b(this._mapPane, new t(0, 0));
                    u = !this._loaded;
                    this._loaded = !0;
                    i = this._limitZoom(i);
                    this.fire("viewprereset");
                    r = this._zoom !== i;
                    this._moveStart(r, !1)._move(n, i)._moveEnd(r);
                    this.fire("viewreset");
                    u && this.fire("load")
                }, _moveStart: function(n, t)
                {
                    return n && this.fire("zoomstart"), t || this.fire("movestart"), this
                }, _move: function(n, t, i)
                {
                    t === undefined && (t = this._zoom);
                    var r = this._zoom !== t;
                    return this._zoom = t, this._lastCenter = n, this._pixelOrigin = this._getNewPixelOrigin(n), (r || i && i.pinch) && this.fire("zoom", i), this.fire("move", i)
                }, _moveEnd: function(n)
                {
                    return n && this.fire("zoomend"), this.fire("moveend")
                }, _stop: function()
                {
                    return nt(this._flyToFrame), this._panAnim && this._panAnim.stop(), this
                }, _rawPanBy: function(n)
                {
                    b(this._mapPane, this._getMapPanePos().subtract(n))
                }, _getZoomSpan: function()
                {
                    return this.getMaxZoom() - this.getMinZoom()
                }, _panInsideMaxBounds: function()
                {
                    this._enforcingBounds || this.panInsideBounds(this.options.maxBounds)
                }, _checkIfLoaded: function()
                {
                    if (!this._loaded)
                        throw new Error("Set map center and zoom first.");
                }, _initEvents: function(n)
                {
                    this._targets = {};
                    this._targets[o(this._container)] = this;
                    var t = n ? w : u;
                    t(this._container, "click dblclick mousedown mouseup mouseover mouseout mousemove contextmenu keypress keydown keyup", this._handleDOMEvent, this);
                    this.options.trackResize && t(window, "resize", this._onResize, this);
                    rt && this.options.transform3DLimit && (n ? this.off : this.on).call(this, "moveend", this._onMoveEnd)
                }, _onResize: function()
                {
                    nt(this._resizeRequest);
                    this._resizeRequest = g(function()
                    {
                        this.invalidateSize({debounceMoveend: !0})
                    }, this)
                }, _onScroll: function()
                {
                    this._container.scrollTop = 0;
                    this._container.scrollLeft = 0
                }, _onMoveEnd: function()
                {
                    var n = this._getMapPanePos();
                    Math.max(Math.abs(n.x), Math.abs(n.y)) >= this.options.transform3DLimit && this._resetView(this.getCenter(), this.getZoom())
                }, _findEventTargets: function(n, t)
                {
                    for (var u = [], r, f = t === "mouseout" || t === "mouseover", i = n.target || n.srcElement, e = !1; i; )
                    {
                        if (r = this._targets[o(i)], r && (t === "click" || t === "preclick") && !n._simulated && this._draggableMoved(r))
                        {
                            e = !0;
                            break
                        }
                        if (r && r.listens(t, !0))
                        {
                            if (f && !tf(i, n))
                                break;
                            if (u.push(r), f)
                                break
                        }
                        if (i === this._container)
                            break;
                        i = i.parentNode
                    }
                    return u.length || e || f || !tf(i, n) || (u = [this]), u
                }, _handleDOMEvent: function(n)
                {
                    if (this._loaded && !io(n))
                    {
                        var t = n.type;
                        (t === "mousedown" || t === "keypress" || t === "keyup" || t === "keydown") && ke(n.target || n.srcElement);
                        this._fireDOMEvent(n, t)
                    }
                }, _mouseEvents: ["click", "dblclick", "mouseover", "mouseout", "contextmenu"], _fireDOMEvent: function(n, t, i)
                {
                    var e,
                        u,
                        r,
                        o,
                        f;
                    if ((n.type === "click" && (e = s({}, n), e.type = "preclick", this._fireDOMEvent(e, e.type, i)), !n._stopped) && (i = (i || []).concat(this._findEventTargets(n, t)), i.length))
                        for (u = i[0], t === "contextmenu" && u.listens(t, !0) && et(n), r = {originalEvent: n}, n.type !== "keypress" && n.type !== "keydown" && n.type !== "keyup" && (o = u.getLatLng && (!u._radius || u._radius <= 10), r.containerPoint = o ? this.latLngToContainerPoint(u.getLatLng()) : this.mouseEventToContainerPoint(n), r.layerPoint = this.containerPointToLayerPoint(r.containerPoint), r.latlng = o ? u.getLatLng() : this.layerPointToLatLng(r.layerPoint)), f = 0; f < i.length; f++)
                            if (i[f].fire(t, r, !0), r.originalEvent._stopped || i[f].options.bubblingMouseEvents === !1 && cs(this._mouseEvents, t) !== -1)
                                return
                }, _draggableMoved: function(n)
                {
                    return n = n.dragging && n.dragging.enabled() ? n : this, n.dragging && n.dragging.moved() || this.boxZoom && this.boxZoom.moved()
                }, _clearHandlers: function()
                {
                    for (var n = 0, t = this._handlers.length; n < t; n++)
                        this._handlers[n].disable()
                }, whenReady: function(n, t)
                {
                    if (this._loaded)
                        n.call(t || this, {target: this});
                    else
                        this.on("load", n, t);
                    return this
                }, _getMapPanePos: function()
                {
                    return oi(this._mapPane) || new t(0, 0)
                }, _moved: function()
                {
                    var n = this._getMapPanePos();
                    return n && !n.equals([0, 0])
                }, _getTopLeftPoint: function(n, t)
                {
                    var i = n && t !== undefined ? this._getNewPixelOrigin(n, t) : this.getPixelOrigin();
                    return i.subtract(this._getMapPanePos())
                }, _getNewPixelOrigin: function(n, t)
                {
                    var i = this.getSize()._divideBy(2);
                    return this.project(n, t)._subtract(i)._add(this._getMapPanePos())._round()
                }, _latLngToNewLayerPoint: function(n, t, i)
                {
                    var r = this._getNewPixelOrigin(i, t);
                    return this.project(n, t)._subtract(r)
                }, _latLngBoundsToNewLayerBounds: function(n, t, i)
                {
                    var r = this._getNewPixelOrigin(i, t);
                    return ct([this.project(n.getSouthWest(), t)._subtract(r), this.project(n.getNorthWest(), t)._subtract(r), this.project(n.getSouthEast(), t)._subtract(r), this.project(n.getNorthEast(), t)._subtract(r)])
                }, _getCenterLayerPoint: function()
                {
                    return this.containerPointToLayerPoint(this.getSize()._divideBy(2))
                }, _getCenterOffset: function(n)
                {
                    return this.latLngToLayerPoint(n).subtract(this._getCenterLayerPoint())
                }, _limitCenter: function(n, t, i)
                {
                    if (!i)
                        return n;
                    var r = this.project(n, t),
                        u = this.getSize().divideBy(2),
                        e = new a(r.subtract(u), r.add(u)),
                        f = this._getBoundsOffset(e, i, t);
                    return f.round().equals([0, 0]) ? n : this.unproject(r.add(f), t)
                }, _limitOffset: function(n, t)
                {
                    if (!t)
                        return n;
                    var i = this.getPixelBounds(),
                        r = new a(i.min.add(n), i.max.add(n));
                    return n.add(this._getBoundsOffset(r, t))
                }, _getBoundsOffset: function(n, i, r)
                {
                    var u = ct(this.project(i.getNorthEast(), r), this.project(i.getSouthWest(), r)),
                        f = u.min.subtract(n.min),
                        e = u.max.subtract(n.max),
                        o = this._rebound(f.x, -e.x),
                        s = this._rebound(f.y, -e.y);
                    return new t(o, s)
                }, _rebound: function(n, t)
                {
                    return n + t > 0 ? Math.round(n - t) / 2 : Math.max(0, Math.ceil(n)) - Math.max(0, Math.floor(t))
                }, _limitZoom: function(n)
                {
                    var i = this.getMinZoom(),
                        r = this.getMaxZoom(),
                        t = rt ? this.options.zoomSnap : 1;
                    return t && (n = Math.round(n / t) * t), Math.max(i, Math.min(r, n))
                }, _onPanTransitionStep: function()
                {
                    this.fire("move")
                }, _onPanTransitionEnd: function()
                {
                    p(this._mapPane, "leaflet-pan-anim");
                    this.fire("moveend")
                }, _tryAnimatedPan: function(n, t)
                {
                    var i = this._getCenterOffset(n)._trunc();
                    return (t && t.animate) !== !0 && !this.getSize().contains(i) ? !1 : (this.panBy(i, t), !0)
                }, _createAnimProxy: function()
                {
                    var n = this._proxy = e("div", "leaflet-proxy leaflet-zoom-animated");
                    this._panes.mapPane.appendChild(n);
                    this.on("zoomanim", function(n)
                    {
                        var t = le,
                            i = this._proxy.style[t];
                        si(this._proxy, this.project(n.center, n.zoom), this.getZoomScale(n.zoom, 1));
                        i === this._proxy.style[t] && this._animatingZoom && this._onZoomTransitionEnd()
                    }, this);
                    this.on("load moveend", function()
                    {
                        var t = this.getCenter(),
                            n = this.getZoom();
                        si(this._proxy, this.project(t, n), this.getZoomScale(n, 1))
                    }, this);
                    this._on("unload", this._destroyAnimProxy, this)
                }, _destroyAnimProxy: function()
                {
                    v(this._proxy);
                    delete this._proxy
                }, _catchTransitionEnd: function(n)
                {
                    this._animatingZoom && n.propertyName.indexOf("transform") >= 0 && this._onZoomTransitionEnd()
                }, _nothingToAnimate: function()
                {
                    return !this._container.getElementsByClassName("leaflet-zoom-animated").length
                }, _tryAnimatedZoom: function(n, t, i)
                {
                    if (this._animatingZoom)
                        return !0;
                    if (i = i || {}, !this._zoomAnimated || i.animate === !1 || this._nothingToAnimate() || Math.abs(t - this._zoom) > this.options.zoomAnimationThreshold)
                        return !1;
                    var r = this.getZoomScale(t),
                        u = this._getCenterOffset(n)._divideBy(1 - 1 / r);
                    return i.animate !== !0 && !this.getSize().contains(u) ? !1 : (g(function()
                        {
                            this._moveStart(!0, !1)._animateZoom(n, t, !0)
                        }, this), !0)
                }, _animateZoom: function(n, t, r, u)
                {
                    this._mapPane && (r && (this._animatingZoom = !0, this._animateToCenter = n, this._animateToZoom = t, i(this._mapPane, "leaflet-zoom-anim")), this.fire("zoomanim", {
                        center: n, zoom: t, noUpdate: u
                    }), setTimeout(c(this._onZoomTransitionEnd, this), 250))
                }, _onZoomTransitionEnd: function()
                {
                    this._animatingZoom && (this._mapPane && p(this._mapPane, "leaflet-zoom-anim"), this._animatingZoom = !1, this._move(this._animateToCenter, this._animateToZoom), g(function()
                        {
                            this._moveEnd(!0)
                        }, this))
                }
        });
    ot = gt.extend({
        options: {position: "topright"}, initialize: function(n)
            {
                l(this, n)
            }, getPosition: function()
            {
                return this.options.position
            }, setPosition: function(n)
            {
                var t = this._map;
                return t && t.removeControl(this), this.options.position = n, t && t.addControl(this), this
            }, getContainer: function()
            {
                return this._container
            }, addTo: function(n)
            {
                this.remove();
                this._map = n;
                var t = this._container = this.onAdd(n),
                    u = this.getPosition(),
                    r = n._controlCorners[u];
                i(t, "leaflet-control");
                u.indexOf("bottom") !== -1 ? r.insertBefore(t, r.firstChild) : r.appendChild(t);
                this._map.on("unload", this.remove, this);
                return this
            }, remove: function()
            {
                if (!this._map)
                    return this;
                if (v(this._container), this.onRemove)
                    this.onRemove(this._map);
                return this._map.off("unload", this.remove, this), this._map = null, this
            }, _refocusOnMap: function(n)
            {
                this._map && n && n.screenX > 0 && n.screenY > 0 && this._map.getContainer().focus()
            }
    });
    ur = function(n)
    {
        return new ot(n)
    };
    f.include({
        addControl: function(n)
        {
            return n.addTo(this), this
        }, removeControl: function(n)
            {
                return n.remove(), this
            }, _initControlPos: function()
            {
                function n(n, u)
                {
                    var f = t + n + " " + t + u;
                    i[n + u] = e("div", f, r)
                }
                var i = this._controlCorners = {},
                    t = "leaflet-",
                    r = this._controlContainer = e("div", t + "control-container", this._container);
                n("top", "left");
                n("top", "right");
                n("bottom", "left");
                n("bottom", "right")
            }, _clearControlPos: function()
            {
                for (var n in this._controlCorners)
                    v(this._controlCorners[n]);
                v(this._controlContainer);
                delete this._controlCorners;
                delete this._controlContainer
            }
    });
    var wh = ot.extend({
            options: {
                collapsed: !0, position: "topright", autoZIndex: !0, hideSingleBase: !1, sortLayers: !1, sortFunction: function(n, t, i, r)
                    {
                        return i < r ? -1 : r < i ? 1 : 0
                    }
            }, initialize: function(n, t, i)
                {
                    l(this, i);
                    this._layerControlInputs = [];
                    this._layers = [];
                    this._lastZIndex = 0;
                    this._handlingClick = !1;
                    for (var r in n)
                        this._addLayer(n[r], r);
                    for (r in t)
                        this._addLayer(t[r], r, !0)
                }, onAdd: function(n)
                {
                    this._initLayout();
                    this._update();
                    this._map = n;
                    n.on("zoomend", this._checkDisabledLayers, this);
                    for (var t = 0; t < this._layers.length; t++)
                        this._layers[t].layer.on("add remove", this._onLayerChange, this);
                    return this._container
                }, addTo: function(n)
                {
                    return ot.prototype.addTo.call(this, n), this._expandIfNotCollapsed()
                }, onRemove: function()
                {
                    this._map.off("zoomend", this._checkDisabledLayers, this);
                    for (var n = 0; n < this._layers.length; n++)
                        this._layers[n].layer.off("add remove", this._onLayerChange, this)
                }, addBaseLayer: function(n, t)
                {
                    return this._addLayer(n, t), this._map ? this._update() : this
                }, addOverlay: function(n, t)
                {
                    return this._addLayer(n, t, !0), this._map ? this._update() : this
                }, removeLayer: function(n)
                {
                    n.off("add remove", this._onLayerChange, this);
                    var t = this._getLayer(o(n));
                    return t && this._layers.splice(this._layers.indexOf(t), 1), this._map ? this._update() : this
                }, expand: function()
                {
                    i(this._container, "leaflet-control-layers-expanded");
                    this._section.style.height = null;
                    var n = this._map.getSize().y - (this._container.offsetTop + 50);
                    return n < this._section.clientHeight ? (i(this._section, "leaflet-control-layers-scrollbar"), this._section.style.height = n + "px") : p(this._section, "leaflet-control-layers-scrollbar"), this._checkDisabledLayers(), this
                }, collapse: function()
                {
                    return p(this._container, "leaflet-control-layers-expanded"), this
                }, _initLayout: function()
                {
                    var n = "leaflet-control-layers",
                        t = this._container = e("div", n),
                        f = this.options.collapsed,
                        r,
                        i;
                    if (t.setAttribute("aria-haspopup", !0), tu(t), no(t), r = this._section = e("section", n + "-list"), f)
                    {
                        this._map.on("click", this.collapse, this);
                        ki || u(t, {
                            mouseenter: this.expand, mouseleave: this.collapse
                        }, this)
                    }
                    i = this._layersLink = e("a", n + "-toggle", t);
                    i.href = "#";
                    i.title = "Layers";
                    pt ? (u(i, "click", bt), u(i, "click", this.expand, this)) : u(i, "focus", this.expand, this);
                    f || this.expand();
                    this._baseLayersList = e("div", n + "-base", r);
                    this._separator = e("div", n + "-separator", r);
                    this._overlaysList = e("div", n + "-overlays", r);
                    t.appendChild(r)
                }, _getLayer: function(n)
                {
                    for (var t = 0; t < this._layers.length; t++)
                        if (this._layers[t] && o(this._layers[t].layer) === n)
                            return this._layers[t]
                }, _addLayer: function(n, t, i)
                {
                    if (this._map)
                        n.on("add remove", this._onLayerChange, this);
                    this._layers.push({
                        layer: n, name: t, overlay: i
                    });
                    this.options.sortLayers && this._layers.sort(c(function(n, t)
                    {
                        return this.options.sortFunction(n.layer, t.layer, n.name, t.name)
                    }, this));
                    this.options.autoZIndex && n.setZIndex && (this._lastZIndex++, n.setZIndex(this._lastZIndex));
                    this._expandIfNotCollapsed()
                }, _update: function()
                {
                    if (!this._container)
                        return this;
                    pu(this._baseLayersList);
                    pu(this._overlaysList);
                    this._layerControlInputs = [];
                    for (var n, r, t, u = 0, i = 0; i < this._layers.length; i++)
                        t = this._layers[i],
                        this._addItem(t),
                        r = r || t.overlay,
                        n = n || !t.overlay,
                        u += t.overlay ? 0 : 1;
                    return this.options.hideSingleBase && (n = n && u > 1, this._baseLayersList.style.display = n ? "" : "none"), this._separator.style.display = r && n ? "" : "none", this
                }, _onLayerChange: function(n)
                {
                    this._handlingClick || this._update();
                    var t = this._getLayer(o(n.target)),
                        i = t.overlay ? n.type === "add" ? "overlayadd" : "overlayremove" : n.type === "add" ? "baselayerchange" : null;
                    i && this._map.fire(i, t)
                }, _createRadioElement: function(n, t)
                {
                    var r = '<input type="radio" class="leaflet-control-layers-selector" name="' + n + '"' + (t ? ' checked="checked"' : "") + "/>",
                        i = document.createElement("div");
                    return i.innerHTML = r, i.firstChild
                }, _addItem: function(n)
                {
                    var r = document.createElement("label"),
                        e = this._map.hasLayer(n.layer),
                        t,
                        f,
                        i,
                        s;
                    return n.overlay ? (t = document.createElement("input"), t.type = "checkbox", t.className = "leaflet-control-layers-selector", t.defaultChecked = e) : t = this._createRadioElement("leaflet-base-layers_" + o(this), e), this._layerControlInputs.push(t), t.layerId = o(n.layer), u(t, "click", this._onInputClick, this), f = document.createElement("span"), f.innerHTML = " " + n.name, i = document.createElement("div"), r.appendChild(i), i.appendChild(t), i.appendChild(f), s = n.overlay ? this._overlaysList : this._baseLayersList, s.appendChild(r), this._checkDisabledLayers(), r
                }, _onInputClick: function()
                {
                    var f = this._layerControlInputs,
                        t,
                        u,
                        i = [],
                        r = [],
                        n;
                    for (this._handlingClick = !0, n = f.length - 1; n >= 0; n--)
                        t = f[n],
                        u = this._getLayer(t.layerId).layer,
                        t.checked ? i.push(u) : t.checked || r.push(u);
                    for (n = 0; n < r.length; n++)
                        this._map.hasLayer(r[n]) && this._map.removeLayer(r[n]);
                    for (n = 0; n < i.length; n++)
                        this._map.hasLayer(i[n]) || this._map.addLayer(i[n]);
                    this._handlingClick = !1;
                    this._refocusOnMap()
                }, _checkDisabledLayers: function()
                {
                    for (var r = this._layerControlInputs, t, n, u = this._map.getZoom(), i = r.length - 1; i >= 0; i--)
                        t = r[i],
                        n = this._getLayer(t.layerId).layer,
                        t.disabled = n.options.minZoom !== undefined && u < n.options.minZoom || n.options.maxZoom !== undefined && u > n.options.maxZoom
                }, _expandIfNotCollapsed: function()
                {
                    return this._map && !this.options.collapsed && this.expand(), this
                }, _expand: function()
                {
                    return this.expand()
                }, _collapse: function()
                {
                    return this.collapse()
                }
        }),
        al = function(n, t, i)
        {
            return new wh(n, t, i)
        },
        uo = ot.extend({
            options: {
                position: "topleft", zoomInText: "+", zoomInTitle: "Zoom in", zoomOutText: "&#x2212;", zoomOutTitle: "Zoom out"
            }, onAdd: function(n)
                {
                    var i = "leaflet-control-zoom",
                        r = e("div", i + " leaflet-bar"),
                        t = this.options;
                    this._zoomInButton = this._createButton(t.zoomInText, t.zoomInTitle, i + "-in", r, this._zoomIn);
                    this._zoomOutButton = this._createButton(t.zoomOutText, t.zoomOutTitle, i + "-out", r, this._zoomOut);
                    this._updateDisabled();
                    n.on("zoomend zoomlevelschange", this._updateDisabled, this);
                    return r
                }, onRemove: function(n)
                {
                    n.off("zoomend zoomlevelschange", this._updateDisabled, this)
                }, disable: function()
                {
                    return this._disabled = !0, this._updateDisabled(), this
                }, enable: function()
                {
                    return this._disabled = !1, this._updateDisabled(), this
                }, _zoomIn: function(n)
                {
                    !this._disabled && this._map._zoom < this._map.getMaxZoom() && this._map.zoomIn(this._map.options.zoomDelta * (n.shiftKey ? 3 : 1))
                }, _zoomOut: function(n)
                {
                    !this._disabled && this._map._zoom > this._map.getMinZoom() && this._map.zoomOut(this._map.options.zoomDelta * (n.shiftKey ? 3 : 1))
                }, _createButton: function(n, t, i, r, f)
                {
                    var o = e("a", i, r);
                    return o.innerHTML = n, o.href = "#", o.title = t, o.setAttribute("role", "button"), o.setAttribute("aria-label", t), tu(o), u(o, "click", bt), u(o, "click", f, this), u(o, "click", this._refocusOnMap, this), o
                }, _updateDisabled: function()
                {
                    var n = this._map,
                        t = "leaflet-disabled";
                    p(this._zoomInButton, t);
                    p(this._zoomOutButton, t);
                    (this._disabled || n._zoom === n.getMinZoom()) && i(this._zoomOutButton, t);
                    (this._disabled || n._zoom === n.getMaxZoom()) && i(this._zoomInButton, t)
                }
        });
    f.mergeOptions({zoomControl: !0});
    f.addInitHook(function()
    {
        this.options.zoomControl && (this.zoomControl = new uo, this.addControl(this.zoomControl))
    });
    var vl = function(n)
        {
            return new uo(n)
        },
        bh = ot.extend({
            options: {
                position: "bottomleft", maxWidth: 100, metric: !0, imperial: !0
            }, onAdd: function(n)
                {
                    var t = "leaflet-control-scale",
                        i = e("div", t),
                        r = this.options;
                    this._addScales(r, t + "-line", i);
                    n.on(r.updateWhenIdle ? "moveend" : "move", this._update, this);
                    return n.whenReady(this._update, this), i
                }, onRemove: function(n)
                {
                    n.off(this.options.updateWhenIdle ? "moveend" : "move", this._update, this)
                }, _addScales: function(n, t, i)
                {
                    n.metric && (this._mScale = e("div", t, i));
                    n.imperial && (this._iScale = e("div", t, i))
                }, _update: function()
                {
                    var n = this._map,
                        t = n.getSize().y / 2,
                        i = n.distance(n.containerPointToLatLng([0, t]), n.containerPointToLatLng([this.options.maxWidth, t]));
                    this._updateScales(i)
                }, _updateScales: function(n)
                {
                    this.options.metric && n && this._updateMetric(n);
                    this.options.imperial && n && this._updateImperial(n)
                }, _updateMetric: function(n)
                {
                    var t = this._getRoundNum(n),
                        i = t < 1e3 ? t + " m" : t / 1e3 + " km";
                    this._updateScale(this._mScale, i, t / n)
                }, _updateImperial: function(n)
                {
                    var t = n * 3.2808399,
                        i,
                        r,
                        u;
                    t > 5280 ? (i = t / 5280, r = this._getRoundNum(i), this._updateScale(this._iScale, r + " mi", r / i)) : (u = this._getRoundNum(t), this._updateScale(this._iScale, u + " ft", u / t))
                }, _updateScale: function(n, t, i)
                {
                    n.style.width = Math.round(this.options.maxWidth * i) + "px";
                    n.innerHTML = t
                }, _getRoundNum: function(n)
                {
                    var i = Math.pow(10, (Math.floor(n) + "").length - 1),
                        t = n / i;
                    return t = t >= 10 ? 10 : t >= 5 ? 5 : t >= 3 ? 3 : t >= 2 ? 2 : 1, i * t
                }
        }),
        yl = function(n)
        {
            return new bh(n)
        },
        fo = ot.extend({
            options: {
                position: "bottomright", prefix: '<a href="https://leafletjs.com" title="A JS library for interactive maps">Leaflet<\/a>'
            }, initialize: function(n)
                {
                    l(this, n);
                    this._attributions = {}
                }, onAdd: function(n)
                {
                    n.attributionControl = this;
                    this._container = e("div", "leaflet-control-attribution");
                    tu(this._container);
                    for (var t in n._layers)
                        n._layers[t].getAttribution && this.addAttribution(n._layers[t].getAttribution());
                    return this._update(), this._container
                }, setPrefix: function(n)
                {
                    return this.options.prefix = n, this._update(), this
                }, addAttribution: function(n)
                {
                    return n ? (this._attributions[n] || (this._attributions[n] = 0), this._attributions[n]++, this._update(), this) : this
                }, removeAttribution: function(n)
                {
                    return n ? (this._attributions[n] && (this._attributions[n]--, this._update()), this) : this
                }, _update: function()
                {
                    var n,
                        i,
                        t;
                    if (this._map)
                    {
                        n = [];
                        for (i in this._attributions)
                            this._attributions[i] && n.push(i);
                        t = [];
                        this.options.prefix && t.push(this.options.prefix);
                        n.length && t.push(n.join(", "));
                        this._container.innerHTML = t.join(" | ")
                    }
                }
        });
    f.mergeOptions({attributionControl: !0});
    f.addInitHook(function()
    {
        this.options.attributionControl && (new fo).addTo(this)
    });
    kh = function(n)
    {
        return new fo(n)
    };
    ot.Layers = wh;
    ot.Zoom = uo;
    ot.Scale = bh;
    ot.Attribution = fo;
    ur.layers = al;
    ur.zoom = vl;
    ur.scale = yl;
    ur.attribution = kh;
    at = gt.extend({
        initialize: function(n)
        {
            this._map = n
        }, enable: function()
            {
                return this._enabled ? this : (this._enabled = !0, this.addHooks(), this)
            }, disable: function()
            {
                return this._enabled ? (this._enabled = !1, this.removeHooks(), this) : this
            }, enabled: function()
            {
                return !!this._enabled
            }
    });
    at.addTo = function(n, t)
    {
        return n.addHandler(t, this), this
    };
    var pl = {Events: tt},
        dh = pt ? "touchstart mousedown" : "mousedown",
        gh = {
            mousedown: "mouseup", touchstart: "touchend", pointerdown: "touchend", MSPointerDown: "touchend"
        },
        eo = {
            mousedown: "mousemove", touchstart: "touchmove", pointerdown: "touchmove", MSPointerDown: "touchmove"
        },
        ci = wi.extend({
            options: {clickTolerance: 3}, initialize: function(n, t, i, r)
                {
                    l(this, r);
                    this._element = n;
                    this._dragStartTarget = t || n;
                    this._preventOutline = i
                }, enable: function()
                {
                    this._enabled || (u(this._dragStartTarget, dh, this._onDown, this), this._enabled = !0)
                }, disable: function()
                {
                    this._enabled && (ci._dragging === this && this.finishDrag(), w(this._dragStartTarget, dh, this._onDown, this), this._enabled = !1, this._moved = !1)
                }, _onDown: function(n)
                {
                    if (!n._simulated && this._enabled && (this._moved = !1, !ae(this._element, "leaflet-zoom-anim")) && !ci._dragging && !n.shiftKey && (n.which === 1 || n.button === 1 || n.touches) && (ci._dragging = this, this._preventOutline && ke(this._element), pe(), gr(), !this._moving))
                    {
                        this.fire("down");
                        var i = n.touches ? n.touches[0] : n,
                            r = ch(this._element);
                        this._startPoint = new t(i.clientX, i.clientY);
                        this._parentScale = de(r);
                        u(document, eo[n.type], this._onMove, this);
                        u(document, gh[n.type], this._onUp, this)
                    }
                }, _onMove: function(n)
                {
                    if (!n._simulated && this._enabled)
                    {
                        if (n.touches && n.touches.length > 1)
                        {
                            this._moved = !0;
                            return
                        }
                        var u = n.touches && n.touches.length === 1 ? n.touches[0] : n,
                            r = new t(u.clientX, u.clientY)._subtract(this._startPoint);
                        (r.x || r.y) && (Math.abs(r.x) + Math.abs(r.y) < this.options.clickTolerance || (r.x /= this._parentScale.x, r.y /= this._parentScale.y, et(n), this._moved || (this.fire("dragstart"), this._moved = !0, this._startPos = oi(this._element).subtract(r), i(document.body, "leaflet-dragging"), this._lastTarget = n.target || n.srcElement, window.SVGElementInstance && this._lastTarget instanceof SVGElementInstance && (this._lastTarget = this._lastTarget.correspondingUseElement), i(this._lastTarget, "leaflet-drag-target")), this._newPos = this._startPos.add(r), this._moving = !0, nt(this._animRequest), this._lastEvent = n, this._animRequest = g(this._updatePosition, this, !0)))
                    }
                }, _updatePosition: function()
                {
                    var n = {originalEvent: this._lastEvent};
                    this.fire("predrag", n);
                    b(this._element, this._newPos);
                    this.fire("drag", n)
                }, _onUp: function(n)
                {
                    !n._simulated && this._enabled && this.finishDrag()
                }, finishDrag: function()
                {
                    p(document.body, "leaflet-dragging");
                    this._lastTarget && (p(this._lastTarget, "leaflet-drag-target"), this._lastTarget = null);
                    for (var n in eo)
                        w(document, eo[n], this._onMove, this),
                        w(document, gh[n], this._onUp, this);
                    we();
                    nu();
                    this._moved && this._moving && (nt(this._animRequest), this.fire("dragend", {distance: this._newPos.distanceTo(this._startPos)}));
                    this._moving = !1;
                    ci._dragging = !1
                }
        });
    fc = (Object.freeze || Object)({
        simplify: nc, pointToSegmentDistance: tc, closestPointOnSegment: wl, clipSegment: rc, _getEdgeIntersection: rf, _getBitCode: li, _sqClosestPointOnSegment: iu, isFlat: ti, _flat: uc
    });
    var gl = (Object.freeze || Object)({clipPolygon: ec}),
        so = {
            project: function(n)
            {
                return new t(n.lng, n.lat)
            }, unproject: function(n)
                {
                    return new h(n.y, n.x)
                }, bounds: new a([-180, -90], [180, 90])
        },
        ho = {
            R: 6378137, R_MINOR: 6356752.3142451793, bounds: new a([-20037508.34279, -15496570.73972], [20037508.34279, 18764656.23138]), project: function(n)
                {
                    var u = Math.PI / 180,
                        r = this.R,
                        i = n.lat * u,
                        f = this.R_MINOR / r,
                        e = Math.sqrt(1 - f * f),
                        o = e * Math.sin(i),
                        s = Math.tan(Math.PI / 4 - i / 2) / Math.pow((1 - o) / (1 + o), e / 2);
                    return i = -r * Math.log(Math.max(s, 1e-10)), new t(n.lng * u * r, i)
                }, unproject: function(n)
                {
                    for (var f = 180 / Math.PI, r = this.R, e = this.R_MINOR / r, o = Math.sqrt(1 - e * e), s = Math.exp(-n.y / r), i = Math.PI / 2 - 2 * Math.atan(s), c = 0, u = .1, t; c < 15 && Math.abs(u) > 1e-7; c++)
                        t = o * Math.sin(i),
                        t = Math.pow((1 - t) / (1 + t), o / 2),
                        u = Math.PI / 2 - 2 * Math.atan(s * t) - i,
                        i += u;
                    return new h(i * f, n.x * f / r)
                }
        },
        na = (Object.freeze || Object)({
            LonLat: so, Mercator: ho, SphericalMercator: kf
        }),
        ta = s({}, ui, {
            code: "EPSG:3395", projection: ho, transformation: function()
                {
                    var n = .5 / (Math.PI * ho.R);
                    return yr(n, .5, -n, .5)
                }()
        }),
        oc = s({}, ui, {
            code: "EPSG:4326", projection: so, transformation: yr(1 / 180, 1, -1 / 180, .5)
        }),
        ia = s({}, ni, {
            projection: so, transformation: yr(1, 0, -1, 0), scale: function(n)
                {
                    return Math.pow(2, n)
                }, zoom: function(n)
                {
                    return Math.log(n) / Math.LN2
                }, distance: function(n, t)
                {
                    var i = t.lng - n.lng,
                        r = t.lat - n.lat;
                    return Math.sqrt(i * i + r * r)
                }, infinite: !0
        });
    ni.Earth = ui;
    ni.EPSG3395 = ta;
    ni.EPSG3857 = hu;
    ni.EPSG900913 = ys;
    ni.EPSG4326 = oc;
    ni.Simple = ia;
    st = wi.extend({
        options: {
            pane: "overlayPane", attribution: null, bubblingMouseEvents: !0
        }, addTo: function(n)
            {
                return n.addLayer(this), this
            }, remove: function()
            {
                return this.removeFrom(this._map || this._mapToAdd)
            }, removeFrom: function(n)
            {
                return n && n.removeLayer(this), this
            }, getPane: function(n)
            {
                return this._map.getPane(n ? this.options[n] || n : this.options.pane)
            }, addInteractiveTarget: function(n)
            {
                return this._map._targets[o(n)] = this, this
            }, removeInteractiveTarget: function(n)
            {
                return delete this._map._targets[o(n)], this
            }, getAttribution: function()
            {
                return this.options.attribution
            }, _layerAdd: function(n)
            {
                var t = n.target,
                    i;
                if (t.hasLayer(this))
                {
                    if (this._map = t, this._zoomAnimated = t._zoomAnimated, this.getEvents)
                    {
                        i = this.getEvents();
                        t.on(i, this);
                        this.once("remove", function()
                        {
                            t.off(i, this)
                        }, this)
                    }
                    this.onAdd(t);
                    this.getAttribution && t.attributionControl && t.attributionControl.addAttribution(this.getAttribution());
                    this.fire("add");
                    t.fire("layeradd", {layer: this})
                }
            }
    });
    f.include({
        addLayer: function(n)
        {
            if (!n._layerAdd)
                throw new Error("The provided object is not a Layer.");
            var t = o(n);
            return this._layers[t] ? this : (this._layers[t] = n, n._mapToAdd = this, n.beforeAdd && n.beforeAdd(this), this.whenReady(n._layerAdd, n), this)
        }, removeLayer: function(n)
            {
                var t = o(n);
                if (!this._layers[t])
                    return this;
                if (this._loaded)
                    n.onRemove(this);
                return n.getAttribution && this.attributionControl && this.attributionControl.removeAttribution(n.getAttribution()), delete this._layers[t], this._loaded && (this.fire("layerremove", {layer: n}), n.fire("remove")), n._map = n._mapToAdd = null, this
            }, hasLayer: function(n)
            {
                return !!n && o(n) in this._layers
            }, eachLayer: function(n, t)
            {
                for (var i in this._layers)
                    n.call(t, this._layers[i]);
                return this
            }, _addLayers: function(n)
            {
                n = n ? ht(n) ? n : [n] : [];
                for (var t = 0, i = n.length; t < i; t++)
                    this.addLayer(n[t])
            }, _addZoomLimit: function(n)
            {
                (isNaN(n.options.maxZoom) || !isNaN(n.options.minZoom)) && (this._zoomBoundLayers[o(n)] = n, this._updateZoomLevels())
            }, _removeZoomLimit: function(n)
            {
                var t = o(n);
                this._zoomBoundLayers[t] && (delete this._zoomBoundLayers[t], this._updateZoomLevels())
            }, _updateZoomLevels: function()
            {
                var n = Infinity,
                    t = -Infinity,
                    u = this._getZoomSpan(),
                    r,
                    i;
                for (r in this._zoomBoundLayers)
                    i = this._zoomBoundLayers[r].options,
                    n = i.minZoom === undefined ? n : Math.min(n, i.minZoom),
                    t = i.maxZoom === undefined ? t : Math.max(t, i.maxZoom);
                this._layersMaxZoom = t === -Infinity ? undefined : t;
                this._layersMinZoom = n === Infinity ? undefined : n;
                u !== this._getZoomSpan() && this.fire("zoomlevelschange");
                this.options.maxZoom === undefined && this._layersMaxZoom && this.getZoom() > this._layersMaxZoom && this.setZoom(this._layersMaxZoom);
                this.options.minZoom === undefined && this._layersMinZoom && this.getZoom() < this._layersMinZoom && this.setZoom(this._layersMinZoom)
            }
    });
    var fr = st.extend({
            initialize: function(n, t)
            {
                l(this, t);
                this._layers = {};
                var i,
                    r;
                if (n)
                    for (i = 0, r = n.length; i < r; i++)
                        this.addLayer(n[i])
            }, addLayer: function(n)
                {
                    var t = this.getLayerId(n);
                    return this._layers[t] = n, this._map && this._map.addLayer(n), this
                }, removeLayer: function(n)
                {
                    var t = n in this._layers ? n : this.getLayerId(n);
                    return this._map && this._layers[t] && this._map.removeLayer(this._layers[t]), delete this._layers[t], this
                }, hasLayer: function(n)
                {
                    return !!n && (n in this._layers || this.getLayerId(n) in this._layers)
                }, clearLayers: function()
                {
                    return this.eachLayer(this.removeLayer, this)
                }, invoke: function(n)
                {
                    var r = Array.prototype.slice.call(arguments, 1),
                        i,
                        t;
                    for (i in this._layers)
                        t = this._layers[i],
                        t[n] && t[n].apply(t, r);
                    return this
                }, onAdd: function(n)
                {
                    this.eachLayer(n.addLayer, n)
                }, onRemove: function(n)
                {
                    this.eachLayer(n.removeLayer, n)
                }, eachLayer: function(n, t)
                {
                    for (var i in this._layers)
                        n.call(t, this._layers[i]);
                    return this
                }, getLayer: function(n)
                {
                    return this._layers[n]
                }, getLayers: function()
                {
                    var n = [];
                    return this.eachLayer(n.push, n), n
                }, setZIndex: function(n)
                {
                    return this.invoke("setZIndex", n)
                }, getLayerId: function(n)
                {
                    return o(n)
                }
        }),
        ra = function(n, t)
        {
            return new fr(n, t)
        },
        er = fr.extend({
            addLayer: function(n)
            {
                return this.hasLayer(n) ? this : (n.addEventParent(this), fr.prototype.addLayer.call(this, n), this.fire("layeradd", {layer: n}))
            }, removeLayer: function(n)
                {
                    return this.hasLayer(n) ? (n in this._layers && (n = this._layers[n]), n.removeEventParent(this), fr.prototype.removeLayer.call(this, n), this.fire("layerremove", {layer: n})) : this
                }, setStyle: function(n)
                {
                    return this.invoke("setStyle", n)
                }, bringToFront: function()
                {
                    return this.invoke("bringToFront")
                }, bringToBack: function()
                {
                    return this.invoke("bringToBack")
                }, getBounds: function()
                {
                    var t = new it,
                        i,
                        n;
                    for (i in this._layers)
                        n = this._layers[i],
                        t.extend(n.getBounds ? n.getBounds() : n.getLatLng());
                    return t
                }
        }),
        ua = function(n)
        {
            return new er(n)
        },
        or = gt.extend({
            options: {
                popupAnchor: [0, 0], tooltipAnchor: [0, 0]
            }, initialize: function(n)
                {
                    l(this, n)
                }, createIcon: function(n)
                {
                    return this._createIcon("icon", n)
                }, createShadow: function(n)
                {
                    return this._createIcon("shadow", n)
                }, _createIcon: function(n, t)
                {
                    var r = this._getIconUrl(n),
                        i;
                    if (!r)
                    {
                        if (n === "icon")
                            throw new Error("iconUrl not set in Icon options (see the docs).");
                        return null
                    }
                    return i = this._createImg(r, t && t.tagName === "IMG" ? t : null), this._setIconStyles(i, n), i
                }, _setIconStyles: function(n, t)
                {
                    var f = this.options,
                        u = f[t + "Size"],
                        i,
                        e;
                    typeof u == "number" && (u = [u, u]);
                    i = r(u);
                    e = r(t === "shadow" && f.shadowAnchor || f.iconAnchor || i && i.divideBy(2, !0));
                    n.className = "leaflet-marker-" + t + " " + (f.className || "");
                    e && (n.style.marginLeft = -e.x + "px", n.style.marginTop = -e.y + "px");
                    i && (n.style.width = i.x + "px", n.style.height = i.y + "px")
                }, _createImg: function(n, t)
                {
                    return t = t || document.createElement("img"), t.src = n, t
                }, _getIconUrl: function(n)
                {
                    return ei && this.options[n + "RetinaUrl"] || this.options[n + "Url"]
                }
        });
    var ru = or.extend({
            options: {
                iconUrl: "marker-icon.png", iconRetinaUrl: "marker-icon-2x.png", shadowUrl: "marker-shadow.png", iconSize: [25, 41], iconAnchor: [12, 41], popupAnchor: [1, -34], tooltipAnchor: [16, -28], shadowSize: [41, 41]
            }, _getIconUrl: function(n)
                {
                    return ru.imagePath || (ru.imagePath = this._detectIconPath()), (this.options.imagePath || ru.imagePath) + or.prototype._getIconUrl.call(this, n)
                }, _detectIconPath: function()
                {
                    var n = e("div", "leaflet-default-icon-path", document.body),
                        t = dr(n, "background-image") || dr(n, "backgroundImage");
                    return document.body.removeChild(n), t === null || t.indexOf("url") !== 0 ? "" : t.replace(/^url\(["']?/, "").replace(/marker-icon\.png["']?\)$/, "")
                }
        }),
        co = at.extend({
            initialize: function(n)
            {
                this._marker = n
            }, addHooks: function()
                {
                    var n = this._marker._icon;
                    this._draggable || (this._draggable = new ci(n, n, !0));
                    this._draggable.on({
                        dragstart: this._onDragStart, predrag: this._onPreDrag, drag: this._onDrag, dragend: this._onDragEnd
                    }, this).enable();
                    i(n, "leaflet-marker-draggable")
                }, removeHooks: function()
                {
                    this._draggable.off({
                        dragstart: this._onDragStart, predrag: this._onPreDrag, drag: this._onDrag, dragend: this._onDragEnd
                    }, this).disable();
                    this._marker._icon && p(this._marker._icon, "leaflet-marker-draggable")
                }, moved: function()
                {
                    return this._draggable && this._draggable._moved
                }, _adjustPan: function(n)
                {
                    var e = this._marker,
                        o = e._map,
                        c = this._marker.options.autoPanSpeed,
                        s = this._marker.options.autoPanPadding,
                        u = oi(e._icon),
                        i = o.getPixelBounds(),
                        h = o.getPixelOrigin(),
                        t = ct(i.min._subtract(h).add(s), i.max._subtract(h).subtract(s)),
                        f;
                    t.contains(u) || (f = r((Math.max(t.max.x, u.x) - t.max.x) / (i.max.x - t.max.x) - (Math.min(t.min.x, u.x) - t.min.x) / (i.min.x - t.min.x), (Math.max(t.max.y, u.y) - t.max.y) / (i.max.y - t.max.y) - (Math.min(t.min.y, u.y) - t.min.y) / (i.min.y - t.min.y)).multiplyBy(c), o.panBy(f, {animate: !1}), this._draggable._newPos._add(f), this._draggable._startPos._add(f), b(e._icon, this._draggable._newPos), this._onDrag(n), this._panRequest = g(this._adjustPan.bind(this, n)))
                }, _onDragStart: function()
                {
                    this._oldLatLng = this._marker.getLatLng();
                    this._marker.closePopup().fire("movestart").fire("dragstart")
                }, _onPreDrag: function(n)
                {
                    this._marker.options.autoPan && (nt(this._panRequest), this._panRequest = g(this._adjustPan.bind(this, n)))
                }, _onDrag: function(n)
                {
                    var t = this._marker,
                        i = t._shadow,
                        r = oi(t._icon),
                        u = t._map.layerPointToLatLng(r);
                    i && b(i, r);
                    t._latlng = u;
                    n.latlng = u;
                    n.oldLatLng = this._oldLatLng;
                    t.fire("move", n).fire("drag", n)
                }, _onDragEnd: function(n)
                {
                    nt(this._panRequest);
                    delete this._oldLatLng;
                    this._marker.fire("moveend").fire("dragend", n)
                }
        }),
        uu = st.extend({
            options: {
                icon: new ru, interactive: !0, keyboard: !0, title: "", alt: "", zIndexOffset: 0, opacity: 1, riseOnHover: !1, riseOffset: 250, pane: "markerPane", shadowPane: "shadowPane", bubblingMouseEvents: !1, draggable: !1, autoPan: !1, autoPanPadding: [50, 50], autoPanSpeed: 10
            }, initialize: function(n, t)
                {
                    l(this, t);
                    this._latlng = y(n)
                }, onAdd: function(n)
                {
                    if (this._zoomAnimated = this._zoomAnimated && n.options.markerZoomAnimation, this._zoomAnimated)
                        n.on("zoomanim", this._animateZoom, this);
                    this._initIcon();
                    this.update()
                }, onRemove: function(n)
                {
                    this.dragging && this.dragging.enabled() && (this.options.draggable = !0, this.dragging.removeHooks());
                    delete this.dragging;
                    this._zoomAnimated && n.off("zoomanim", this._animateZoom, this);
                    this._removeIcon();
                    this._removeShadow()
                }, getEvents: function()
                {
                    return {
                            zoom: this.update, viewreset: this.update
                        }
                }, getLatLng: function()
                {
                    return this._latlng
                }, setLatLng: function(n)
                {
                    var t = this._latlng;
                    return this._latlng = y(n), this.update(), this.fire("move", {
                                oldLatLng: t, latlng: this._latlng
                            })
                }, setZIndexOffset: function(n)
                {
                    return this.options.zIndexOffset = n, this.update()
                }, getIcon: function()
                {
                    return this.options.icon
                }, setIcon: function(n)
                {
                    return this.options.icon = n, this._map && (this._initIcon(), this.update()), this._popup && this.bindPopup(this._popup, this._popup.options), this
                }, getElement: function()
                {
                    return this._icon
                }, update: function()
                {
                    if (this._icon && this._map)
                    {
                        var n = this._map.latLngToLayerPoint(this._latlng).round();
                        this._setPos(n)
                    }
                    return this
                }, _initIcon: function()
                {
                    var n = this.options,
                        f = "leaflet-zoom-" + (this._zoomAnimated ? "animated" : "hide"),
                        t = n.icon.createIcon(this._icon),
                        e = !1,
                        r,
                        u;
                    if (t !== this._icon && (this._icon && this._removeIcon(), e = !0, n.title && (t.title = n.title), t.tagName === "IMG" && (t.alt = n.alt || "")), i(t, f), n.keyboard && (t.tabIndex = "0"), this._icon = t, n.riseOnHover)
                        this.on({
                            mouseover: this._bringToFront, mouseout: this._resetZIndex
                        });
                    r = n.icon.createShadow(this._shadow);
                    u = !1;
                    r !== this._shadow && (this._removeShadow(), u = !0);
                    r && (i(r, f), r.alt = "");
                    this._shadow = r;
                    n.opacity < 1 && this._updateOpacity();
                    e && this.getPane().appendChild(this._icon);
                    this._initInteraction();
                    r && u && this.getPane(n.shadowPane).appendChild(this._shadow)
                }, _removeIcon: function()
                {
                    this.options.riseOnHover && this.off({
                        mouseover: this._bringToFront, mouseout: this._resetZIndex
                    });
                    v(this._icon);
                    this.removeInteractiveTarget(this._icon);
                    this._icon = null
                }, _removeShadow: function()
                {
                    this._shadow && v(this._shadow);
                    this._shadow = null
                }, _setPos: function(n)
                {
                    b(this._icon, n);
                    this._shadow && b(this._shadow, n);
                    this._zIndex = n.y + this.options.zIndexOffset;
                    this._resetZIndex()
                }, _updateZIndex: function(n)
                {
                    this._icon.style.zIndex = this._zIndex + n
                }, _animateZoom: function(n)
                {
                    var t = this._map._latLngToNewLayerPoint(this._latlng, n.zoom, n.center).round();
                    this._setPos(t)
                }, _initInteraction: function()
                {
                    if (this.options.interactive && (i(this._icon, "leaflet-interactive"), this.addInteractiveTarget(this._icon), co))
                    {
                        var n = this.options.draggable;
                        this.dragging && (n = this.dragging.enabled(), this.dragging.disable());
                        this.dragging = new co(this);
                        n && this.dragging.enable()
                    }
                }, setOpacity: function(n)
                {
                    return this.options.opacity = n, this._map && this._updateOpacity(), this
                }, _updateOpacity: function()
                {
                    var n = this.options.opacity;
                    this._icon && ut(this._icon, n);
                    this._shadow && ut(this._shadow, n)
                }, _bringToFront: function()
                {
                    this._updateZIndex(this.options.riseOffset)
                }, _resetZIndex: function()
                {
                    this._updateZIndex(0)
                }, _getPopupAnchor: function()
                {
                    return this.options.icon.options.popupAnchor
                }, _getTooltipAnchor: function()
                {
                    return this.options.icon.options.tooltipAnchor
                }
        });
    ii = st.extend({
        options: {
            stroke: !0, color: "#3388ff", weight: 3, opacity: 1, lineCap: "round", lineJoin: "round", dashArray: null, dashOffset: null, fill: !1, fillColor: null, fillOpacity: .2, fillRule: "evenodd", interactive: !0, bubblingMouseEvents: !0
        }, beforeAdd: function(n)
            {
                this._renderer = n.getRenderer(this)
            }, onAdd: function()
            {
                this._renderer._initPath(this);
                this._reset();
                this._renderer._addPath(this)
            }, onRemove: function()
            {
                this._renderer._removePath(this)
            }, redraw: function()
            {
                return this._map && this._renderer._updatePath(this), this
            }, setStyle: function(n)
            {
                return l(this, n), this._renderer && (this._renderer._updateStyle(this), this.options.stroke && n.hasOwnProperty("weight") && this._updateBounds()), this
            }, bringToFront: function()
            {
                return this._renderer && this._renderer._bringToFront(this), this
            }, bringToBack: function()
            {
                return this._renderer && this._renderer._bringToBack(this), this
            }, getElement: function()
            {
                return this._path
            }, _reset: function()
            {
                this._project();
                this._update()
            }, _clickTolerance: function()
            {
                return (this.options.stroke ? this.options.weight / 2 : 0) + this._renderer.options.tolerance
            }
    });
    fu = ii.extend({
        options: {
            fill: !0, radius: 10
        }, initialize: function(n, t)
            {
                l(this, t);
                this._latlng = y(n);
                this._radius = this.options.radius
            }, setLatLng: function(n)
            {
                return this._latlng = y(n), this.redraw(), this.fire("move", {latlng: this._latlng})
            }, getLatLng: function()
            {
                return this._latlng
            }, setRadius: function(n)
            {
                return this.options.radius = this._radius = n, this.redraw()
            }, getRadius: function()
            {
                return this._radius
            }, setStyle: function(n)
            {
                var t = n && n.radius || this._radius;
                return ii.prototype.setStyle.call(this, n), this.setRadius(t), this
            }, _project: function()
            {
                this._point = this._map.latLngToLayerPoint(this._latlng);
                this._updateBounds()
            }, _updateBounds: function()
            {
                var n = this._radius,
                    r = this._radiusY || n,
                    t = this._clickTolerance(),
                    i = [n + t, r + t];
                this._pxBounds = new a(this._point.subtract(i), this._point.add(i))
            }, _update: function()
            {
                this._map && this._updatePath()
            }, _updatePath: function()
            {
                this._renderer._updateCircle(this)
            }, _empty: function()
            {
                return this._radius && !this._renderer._bounds.intersects(this._pxBounds)
            }, _containsPoint: function(n)
            {
                return n.distanceTo(this._point) <= this._radius + this._clickTolerance()
            }
    });
    uf = fu.extend({
        initialize: function(n, t, i)
        {
            if (typeof t == "number" && (t = s({}, i, {radius: t})), l(this, t), this._latlng = y(n), isNaN(this.options.radius))
                throw new Error("Circle radius cannot be NaN");
            this._mRadius = this.options.radius
        }, setRadius: function(n)
            {
                return this._mRadius = n, this.redraw()
            }, getRadius: function()
            {
                return this._mRadius
            }, getBounds: function()
            {
                var n = [this._radius, this._radiusY || this._radius];
                return new it(this._map.layerPointToLatLng(this._point.subtract(n)), this._map.layerPointToLatLng(this._point.add(n)))
            }, setStyle: ii.prototype.setStyle, _project: function()
            {
                var e = this._latlng.lng,
                    i = this._latlng.lat,
                    n = this._map,
                    o = n.options.crs,
                    c;
                if (o.distance === ui.distance)
                {
                    var t = Math.PI / 180,
                        u = this._mRadius / ui.R / t,
                        h = n.project([i + u, e]),
                        l = n.project([i - u, e]),
                        f = h.add(l).divideBy(2),
                        s = n.unproject(f).lat,
                        r = Math.acos((Math.cos(u * t) - Math.sin(i * t) * Math.sin(s * t)) / (Math.cos(i * t) * Math.cos(s * t))) / t;
                    (isNaN(r) || r === 0) && (r = u / Math.cos(Math.PI / 180 * i));
                    this._point = f.subtract(n.getPixelOrigin());
                    this._radius = isNaN(r) ? 0 : f.x - n.project([s, e - r]).x;
                    this._radiusY = f.y - h.y
                }
                else
                    c = o.unproject(o.project(this._latlng).subtract([this._mRadius, 0])),
                    this._point = n.latLngToLayerPoint(this._latlng),
                    this._radius = this._point.x - n.latLngToLayerPoint(c).x;
                this._updateBounds()
            }
    });
    kt = ii.extend({
        options: {
            smoothFactor: 1, noClip: !1
        }, initialize: function(n, t)
            {
                l(this, t);
                this._setLatLngs(n)
            }, getLatLngs: function()
            {
                return this._latlngs
            }, setLatLngs: function(n)
            {
                return this._setLatLngs(n), this.redraw()
            }, isEmpty: function()
            {
                return !this._latlngs.length
            }, closestLayerPoint: function(n)
            {
                for (var r, t, c, s, u = Infinity, i = null, h = iu, f, e, o = 0, l = this._parts.length; o < l; o++)
                    for (r = this._parts[o], t = 1, c = r.length; t < c; t++)
                        f = r[t - 1],
                        e = r[t],
                        s = h(n, f, e, !0),
                        s < u && (u = s, i = h(n, f, e));
                return i && (i.distance = Math.sqrt(u)), i
            }, getCenter: function()
            {
                if (!this._map)
                    throw new Error("Must add layer to map before using getCenter()");
                var n,
                    r,
                    e,
                    u,
                    f,
                    t,
                    o,
                    i = this._rings[0],
                    s = i.length;
                if (!s)
                    return null;
                for (n = 0, r = 0; n < s - 1; n++)
                    r += i[n].distanceTo(i[n + 1]) / 2;
                if (r === 0)
                    return this._map.layerPointToLatLng(i[0]);
                for (n = 0, u = 0; n < s - 1; n++)
                    if (f = i[n], t = i[n + 1], e = f.distanceTo(t), u += e, u > r)
                        return o = (u - r) / e, this._map.layerPointToLatLng([t.x - o * (t.x - f.x), t.y - o * (t.y - f.y)])
            }, getBounds: function()
            {
                return this._bounds
            }, addLatLng: function(n, t)
            {
                return t = t || this._defaultShape(), n = y(n), t.push(n), this._bounds.extend(n), this.redraw()
            }, _setLatLngs: function(n)
            {
                this._bounds = new it;
                this._latlngs = this._convertLatLngs(n)
            }, _defaultShape: function()
            {
                return ti(this._latlngs) ? this._latlngs : this._latlngs[0]
            }, _convertLatLngs: function(n)
            {
                for (var i = [], r = ti(n), t = 0, u = n.length; t < u; t++)
                    r ? (i[t] = y(n[t]), this._bounds.extend(i[t])) : i[t] = this._convertLatLngs(n[t]);
                return i
            }, _project: function()
            {
                var n = new a;
                this._rings = [];
                this._projectLatlngs(this._latlngs, this._rings, n);
                this._bounds.isValid() && n.isValid() && (this._rawPxBounds = n, this._updateBounds())
            }, _updateBounds: function()
            {
                var n = this._clickTolerance(),
                    i = new t(n, n);
                this._pxBounds = new a([this._rawPxBounds.min.subtract(i), this._rawPxBounds.max.add(i)])
            }, _projectLatlngs: function(n, t, i)
            {
                var e = n[0] instanceof h,
                    f = n.length,
                    r,
                    u;
                if (e)
                {
                    for (u = [], r = 0; r < f; r++)
                        u[r] = this._map.latLngToLayerPoint(n[r]),
                        i.extend(u[r]);
                    t.push(u)
                }
                else
                    for (r = 0; r < f; r++)
                        this._projectLatlngs(n[r], t, i)
            }, _clipPoints: function()
            {
                var o = this._renderer._bounds,
                    i,
                    f,
                    n,
                    t,
                    s,
                    e,
                    r,
                    u;
                if (this._parts = [], this._pxBounds && this._pxBounds.intersects(o))
                {
                    if (this.options.noClip)
                    {
                        this._parts = this._rings;
                        return
                    }
                    for (i = this._parts, f = 0, t = 0, s = this._rings.length; f < s; f++)
                        for (u = this._rings[f], n = 0, e = u.length; n < e - 1; n++)
                            (r = rc(u[n], u[n + 1], o, n, !0), r) && (i[t] = i[t] || [], i[t].push(r[0]), (r[1] !== u[n + 1] || n === e - 2) && (i[t].push(r[1]), t++))
                }
            }, _simplifyPoints: function()
            {
                for (var t = this._parts, i = this.options.smoothFactor, n = 0, r = t.length; n < r; n++)
                    t[n] = nc(t[n], i)
            }, _update: function()
            {
                this._map && (this._clipPoints(), this._simplifyPoints(), this._updatePath())
            }, _updatePath: function()
            {
                this._renderer._updatePoly(this)
            }, _containsPoint: function(n, t)
            {
                var r,
                    i,
                    f,
                    o,
                    e,
                    u,
                    s = this._clickTolerance();
                if (!this._pxBounds || !this._pxBounds.contains(n))
                    return !1;
                for (r = 0, o = this._parts.length; r < o; r++)
                    for (u = this._parts[r], i = 0, e = u.length, f = e - 1; i < e; f = i++)
                        if ((t || i !== 0) && tc(n, u[f], u[i]) <= s)
                            return !0;
                return !1
            }
    });
    kt._flat = uc;
    ai = kt.extend({
        options: {fill: !0}, isEmpty: function()
            {
                return !this._latlngs.length || !this._latlngs[0].length
            }, getCenter: function()
            {
                if (!this._map)
                    throw new Error("Must add layer to map before using getCenter()");
                var r,
                    e,
                    n,
                    t,
                    u,
                    i,
                    o,
                    s,
                    c,
                    f = this._rings[0],
                    h = f.length;
                if (!h)
                    return null;
                for (i = o = s = 0, r = 0, e = h - 1; r < h; e = r++)
                    n = f[r],
                    t = f[e],
                    u = n.y * t.x - t.y * n.x,
                    o += (n.x + t.x) * u,
                    s += (n.y + t.y) * u,
                    i += u * 3;
                return c = i === 0 ? f[0] : [o / i, s / i], this._map.layerPointToLatLng(c)
            }, _convertLatLngs: function(n)
            {
                var t = kt.prototype._convertLatLngs.call(this, n),
                    i = t.length;
                return i >= 2 && t[0] instanceof h && t[0].equals(t[i - 1]) && t.pop(), t
            }, _setLatLngs: function(n)
            {
                kt.prototype._setLatLngs.call(this, n);
                ti(this._latlngs) && (this._latlngs = [this._latlngs])
            }, _defaultShape: function()
            {
                return ti(this._latlngs[0]) ? this._latlngs[0] : this._latlngs[0][0]
            }, _clipPoints: function()
            {
                var n = this._renderer._bounds,
                    u = this.options.weight,
                    f = new t(u, u),
                    i,
                    e,
                    r;
                if (n = new a(n.min.subtract(f), n.max.add(f)), this._parts = [], this._pxBounds && this._pxBounds.intersects(n))
                {
                    if (this.options.noClip)
                    {
                        this._parts = this._rings;
                        return
                    }
                    for (i = 0, e = this._rings.length; i < e; i++)
                        r = ec(this._rings[i], n, !0),
                        r.length && this._parts.push(r)
                }
            }, _updatePath: function()
            {
                this._renderer._updatePoly(this, !0)
            }, _containsPoint: function(n)
            {
                var e = !1,
                    i,
                    t,
                    r,
                    u,
                    f,
                    o,
                    h,
                    s;
                if (!this._pxBounds || !this._pxBounds.contains(n))
                    return !1;
                for (u = 0, h = this._parts.length; u < h; u++)
                    for (i = this._parts[u], f = 0, s = i.length, o = s - 1; f < s; o = f++)
                        t = i[f],
                        r = i[o],
                        t.y > n.y != r.y > n.y && n.x < (r.x - t.x) * (n.y - t.y) / (r.y - t.y) + t.x && (e = !e);
                return e || kt.prototype._containsPoint.call(this, n, !0)
            }
    });
    dt = er.extend({
        initialize: function(n, t)
        {
            l(this, t);
            this._layers = {};
            n && this.addData(n)
        }, addData: function(n)
            {
                var f = ht(n) ? n : n.features,
                    u,
                    e,
                    i,
                    r,
                    t;
                if (f)
                {
                    for (u = 0, e = f.length; u < e; u++)
                        i = f[u],
                        (i.geometries || i.geometry || i.features || i.coordinates) && this.addData(i);
                    return this
                }
                if ((r = this.options, r.filter && !r.filter(n)) || (t = lo(n, r), !t))
                    return this;
                if (t.feature = of(n), t.defaultOptions = t.options, this.resetStyle(t), r.onEachFeature)
                    r.onEachFeature(n, t);
                return this.addLayer(t)
            }, resetStyle: function(n)
            {
                return n.options = s({}, n.defaultOptions), this._setLayerStyle(n, this.options.style), this
            }, setStyle: function(n)
            {
                return this.eachLayer(function(t)
                    {
                        this._setLayerStyle(t, n)
                    }, this)
            }, _setLayerStyle: function(n, t)
            {
                n.setStyle && (typeof t == "function" && (t = t(n.feature)), n.setStyle(t))
            }
    });
    sf = {toGeoJSON: function(n)
        {
            return sr(this, {
                    type: "Point", coordinates: vo(this.getLatLng(), n)
                })
        }};
    uu.include(sf);
    uf.include(sf);
    fu.include(sf);
    kt.include({toGeoJSON: function(n)
        {
            var t = !ti(this._latlngs),
                i = ef(this._latlngs, t ? 1 : 0, !1, n);
            return sr(this, {
                    type: (t ? "Multi" : "") + "LineString", coordinates: i
                })
        }});
    ai.include({toGeoJSON: function(n)
        {
            var t = !ti(this._latlngs),
                r = t && !ti(this._latlngs[0]),
                i = ef(this._latlngs, r ? 2 : t ? 1 : 0, !0, n);
            return t || (i = [i]), sr(this, {
                    type: (r ? "Multi" : "") + "Polygon", coordinates: i
                })
        }});
    fr.include({
        toMultiPoint: function(n)
        {
            var t = [];
            return this.eachLayer(function(i)
                {
                    t.push(i.toGeoJSON(n).geometry.coordinates)
                }), sr(this, {
                    type: "MultiPoint", coordinates: t
                })
        }, toGeoJSON: function(n)
            {
                var r = this.feature && this.feature.geometry && this.feature.geometry.type,
                    i,
                    t;
                return r === "MultiPoint" ? this.toMultiPoint(n) : (i = r === "GeometryCollection", t = [], this.eachLayer(function(r)
                        {
                            var f,
                                u;
                            r.toGeoJSON && (f = r.toGeoJSON(n), i ? t.push(f.geometry) : (u = of(f), u.type === "FeatureCollection" ? t.push.apply(t, u.features) : t.push(u)))
                        }), i) ? sr(this, {
                        geometries: t, type: "GeometryCollection"
                    }) : {
                        type: "FeatureCollection", features: t
                    }
            }
    });
    var la = sc,
        hf = st.extend({
            options: {
                opacity: 1, alt: "", interactive: !1, crossOrigin: !1, errorOverlayUrl: "", zIndex: 1, className: ""
            }, initialize: function(n, t, i)
                {
                    this._url = n;
                    this._bounds = d(t);
                    l(this, i)
                }, onAdd: function()
                {
                    this._image || (this._initImage(), this.options.opacity < 1 && this._updateOpacity());
                    this.options.interactive && (i(this._image, "leaflet-interactive"), this.addInteractiveTarget(this._image));
                    this.getPane().appendChild(this._image);
                    this._reset()
                }, onRemove: function()
                {
                    v(this._image);
                    this.options.interactive && this.removeInteractiveTarget(this._image)
                }, setOpacity: function(n)
                {
                    return this.options.opacity = n, this._image && this._updateOpacity(), this
                }, setStyle: function(n)
                {
                    return n.opacity && this.setOpacity(n.opacity), this
                }, bringToFront: function()
                {
                    return this._map && tr(this._image), this
                }, bringToBack: function()
                {
                    return this._map && ir(this._image), this
                }, setUrl: function(n)
                {
                    return this._url = n, this._image && (this._image.src = n), this
                }, setBounds: function(n)
                {
                    return this._bounds = d(n), this._map && this._reset(), this
                }, getEvents: function()
                {
                    var n = {
                            zoom: this._reset, viewreset: this._reset
                        };
                    return this._zoomAnimated && (n.zoomanim = this._animateZoom), n
                }, setZIndex: function(n)
                {
                    return this.options.zIndex = n, this._updateZIndex(), this
                }, getBounds: function()
                {
                    return this._bounds
                }, getElement: function()
                {
                    return this._image
                }, _initImage: function()
                {
                    var t = this._url.tagName === "IMG",
                        n = this._image = t ? this._url : e("img");
                    if (i(n, "leaflet-image-layer"), this._zoomAnimated && i(n, "leaflet-zoom-animated"), this.options.className && i(n, this.options.className), n.onselectstart = k, n.onmousemove = k, n.onload = c(this.fire, this, "load"), n.onerror = c(this._overlayOnError, this, "error"), (this.options.crossOrigin || this.options.crossOrigin === "") && (n.crossOrigin = this.options.crossOrigin === !0 ? "" : this.options.crossOrigin), this.options.zIndex && this._updateZIndex(), t)
                    {
                        this._url = n.src;
                        return
                    }
                    n.src = this._url;
                    n.alt = this.options.alt
                }, _animateZoom: function(n)
                {
                    var t = this._map.getZoomScale(n.zoom),
                        i = this._map._latLngBoundsToNewLayerBounds(this._bounds, n.zoom, n.center).min;
                    si(this._image, i, t)
                }, _reset: function()
                {
                    var n = this._image,
                        t = new a(this._map.latLngToLayerPoint(this._bounds.getNorthWest()), this._map.latLngToLayerPoint(this._bounds.getSouthEast())),
                        i = t.getSize();
                    b(n, t.min);
                    n.style.width = i.x + "px";
                    n.style.height = i.y + "px"
                }, _updateOpacity: function()
                {
                    ut(this._image, this.options.opacity)
                }, _updateZIndex: function()
                {
                    this._image && this.options.zIndex !== undefined && this.options.zIndex !== null && (this._image.style.zIndex = this.options.zIndex)
                }, _overlayOnError: function()
                {
                    this.fire("error");
                    var n = this.options.errorOverlayUrl;
                    n && this._url !== n && (this._url = n, this._image.src = n)
                }
        }),
        aa = function(n, t, i)
        {
            return new hf(n, t, i)
        },
        hc = hf.extend({
            options: {
                autoplay: !0, loop: !0, keepAspectRatio: !0
            }, _initImage: function()
                {
                    var s = this._url.tagName === "VIDEO",
                        n = this._image = s ? this._url : e("video"),
                        t,
                        f,
                        r,
                        u,
                        o;
                    if (i(n, "leaflet-image-layer"), this._zoomAnimated && i(n, "leaflet-zoom-animated"), n.onselectstart = k, n.onmousemove = k, n.onloadeddata = c(this.fire, this, "load"), s)
                    {
                        for (t = n.getElementsByTagName("source"), f = [], r = 0; r < t.length; r++)
                            f.push(t[r].src);
                        this._url = t.length > 0 ? f : [n.src];
                        return
                    }
                    for (ht(this._url) || (this._url = [this._url]), !this.options.keepAspectRatio && n.style.hasOwnProperty("objectFit") && (n.style.objectFit = "fill"), n.autoplay = !!this.options.autoplay, n.loop = !!this.options.loop, u = 0; u < this._url.length; u++)
                        o = e("source"),
                        o.src = this._url[u],
                        n.appendChild(o)
                }
        });
    yo = hf.extend({_initImage: function()
        {
            var n = this._image = this._url;
            i(n, "leaflet-image-layer");
            this._zoomAnimated && i(n, "leaflet-zoom-animated");
            n.onselectstart = k;
            n.onmousemove = k
        }});
    var ri = st.extend({
            options: {
                offset: [0, 7], className: "", pane: "popupPane"
            }, initialize: function(n, t)
                {
                    l(this, n);
                    this._source = t
                }, onAdd: function(n)
                {
                    this._zoomAnimated = n._zoomAnimated;
                    this._container || this._initLayout();
                    n._fadeAnimated && ut(this._container, 0);
                    clearTimeout(this._removeTimeout);
                    this.getPane().appendChild(this._container);
                    this.update();
                    n._fadeAnimated && ut(this._container, 1);
                    this.bringToFront()
                }, onRemove: function(n)
                {
                    n._fadeAnimated ? (ut(this._container, 0), this._removeTimeout = setTimeout(c(v, undefined, this._container), 200)) : v(this._container)
                }, getLatLng: function()
                {
                    return this._latlng
                }, setLatLng: function(n)
                {
                    return this._latlng = y(n), this._map && (this._updatePosition(), this._adjustPan()), this
                }, getContent: function()
                {
                    return this._content
                }, setContent: function(n)
                {
                    return this._content = n, this.update(), this
                }, getElement: function()
                {
                    return this._container
                }, update: function()
                {
                    this._map && (this._container.style.visibility = "hidden", this._updateContent(), this._updateLayout(), this._updatePosition(), this._container.style.visibility = "", this._adjustPan())
                }, getEvents: function()
                {
                    var n = {
                            zoom: this._updatePosition, viewreset: this._updatePosition
                        };
                    return this._zoomAnimated && (n.zoomanim = this._animateZoom), n
                }, isOpen: function()
                {
                    return !!this._map && this._map.hasLayer(this)
                }, bringToFront: function()
                {
                    return this._map && tr(this._container), this
                }, bringToBack: function()
                {
                    return this._map && ir(this._container), this
                }, _prepareOpen: function(n, t, i)
                {
                    if (t instanceof st || (i = t, t = n), t instanceof er)
                        for (var r in n._layers)
                        {
                            t = n._layers[r];
                            break
                        }
                    if (!i)
                        if (t.getCenter)
                            i = t.getCenter();
                        else if (t.getLatLng)
                            i = t.getLatLng();
                        else
                            throw new Error("Unable to get source layer LatLng.");
                    return this._source = t, this.update(), i
                }, _updateContent: function()
                {
                    if (this._content)
                    {
                        var n = this._contentNode,
                            t = typeof this._content == "function" ? this._content(this._source || this) : this._content;
                        if (typeof t == "string")
                            n.innerHTML = t;
                        else
                        {
                            while (n.hasChildNodes())
                                n.removeChild(n.firstChild);
                            n.appendChild(t)
                        }
                        this.fire("contentupdate")
                    }
                }, _updatePosition: function()
                {
                    var u,
                        f;
                    if (this._map)
                    {
                        var t = this._map.latLngToLayerPoint(this._latlng),
                            n = r(this.options.offset),
                            i = this._getAnchor();
                        this._zoomAnimated ? b(this._container, t.add(i)) : n = n.add(t).add(i);
                        u = this._containerBottom = -n.y;
                        f = this._containerLeft = -Math.round(this._containerWidth / 2) + n.x;
                        this._container.style.bottom = u + "px";
                        this._container.style.left = f + "px"
                    }
                }, _getAnchor: function()
                {
                    return [0, 0]
                }
        }),
        hr = ri.extend({
            options: {
                maxWidth: 300, minWidth: 50, maxHeight: null, autoPan: !0, autoPanPaddingTopLeft: null, autoPanPaddingBottomRight: null, autoPanPadding: [5, 5], keepInView: !1, closeButton: !0, autoClose: !0, closeOnEscapeKey: !0, className: ""
            }, openOn: function(n)
                {
                    return n.openPopup(this), this
                }, onAdd: function(n)
                {
                    if (ri.prototype.onAdd.call(this, n), n.fire("popupopen", {popup: this}), this._source && (this._source.fire("popupopen", {popup: this}, !0), !(this._source instanceof ii)))
                        this._source.on("preclick", hi)
                }, onRemove: function(n)
                {
                    ri.prototype.onRemove.call(this, n);
                    n.fire("popupclose", {popup: this});
                    this._source && (this._source.fire("popupclose", {popup: this}, !0), this._source instanceof ii || this._source.off("preclick", hi))
                }, getEvents: function()
                {
                    var n = ri.prototype.getEvents.call(this);
                    return (this.options.closeOnClick !== undefined ? this.options.closeOnClick : this._map.options.closePopupOnClick) && (n.preclick = this._close), this.options.keepInView && (n.moveend = this._adjustPan), n
                }, _close: function()
                {
                    this._map && this._map.closePopup(this)
                }, _initLayout: function()
                {
                    var n = "leaflet-popup",
                        i = this._container = e("div", n + " " + (this.options.className || "") + " leaflet-zoom-animated"),
                        r = this._wrapper = e("div", n + "-content-wrapper", i),
                        t;
                    this._contentNode = e("div", n + "-content", r);
                    tu(r);
                    no(this._contentNode);
                    u(r, "contextmenu", hi);
                    this._tipContainer = e("div", n + "-tip-container", i);
                    this._tip = e("div", n + "-tip", this._tipContainer);
                    this.options.closeButton && (t = this._closeButton = e("a", n + "-close-button", i), t.href = "#close", t.innerHTML = "&#215;", u(t, "click", this._onCloseButtonClick, this))
                }, _updateLayout: function()
                {
                    var r = this._contentNode,
                        n = r.style,
                        t;
                    n.width = "";
                    n.whiteSpace = "nowrap";
                    t = r.offsetWidth;
                    t = Math.min(t, this.options.maxWidth);
                    t = Math.max(t, this.options.minWidth);
                    n.width = t + 1 + "px";
                    n.whiteSpace = "";
                    n.height = "";
                    var e = r.offsetHeight,
                        u = this.options.maxHeight,
                        f = "leaflet-popup-scrolled";
                    u && e > u ? (n.height = u + "px", i(r, f)) : p(r, f);
                    this._containerWidth = this._container.offsetWidth
                }, _animateZoom: function(n)
                {
                    var t = this._map._latLngToNewLayerPoint(this._latlng, n.zoom, n.center),
                        i = this._getAnchor();
                    b(this._container, t.add(i))
                }, _adjustPan: function()
                {
                    if (this.options.autoPan)
                    {
                        this._map._panAnim && this._map._panAnim.stop();
                        var s = this._map,
                            v = parseInt(dr(this._container, "marginBottom"), 10) || 0,
                            h = this._container.offsetHeight + v,
                            c = this._containerWidth,
                            l = new t(this._containerLeft, -h - this._containerBottom);
                        l._add(oi(this._container));
                        var n = s.layerPointToContainerPoint(l),
                            a = r(this.options.autoPanPadding),
                            f = r(this.options.autoPanPaddingTopLeft || a),
                            e = r(this.options.autoPanPaddingBottomRight || a),
                            o = s.getSize(),
                            i = 0,
                            u = 0;
                        n.x + c + e.x > o.x && (i = n.x + c - o.x + e.x);
                        n.x - i - f.x < 0 && (i = n.x - f.x);
                        n.y + h + e.y > o.y && (u = n.y + h - o.y + e.y);
                        n.y - u - f.y < 0 && (u = n.y - f.y);
                        (i || u) && s.fire("autopanstart").panBy([i, u])
                    }
                }, _onCloseButtonClick: function(n)
                {
                    this._close();
                    bt(n)
                }, _getAnchor: function()
                {
                    return r(this._source && this._source._getPopupAnchor ? this._source._getPopupAnchor() : [0, 0])
                }
        }),
        pa = function(n, t)
        {
            return new hr(n, t)
        };
    f.mergeOptions({closePopupOnClick: !0});
    f.include({
        openPopup: function(n, t, i)
        {
            return (n instanceof hr || (n = new hr(i).setContent(n)), t && n.setLatLng(t), this.hasLayer(n)) ? this : (this._popup && this._popup.options.autoClose && this.closePopup(), this._popup = n, this.addLayer(n))
        }, closePopup: function(n)
            {
                return n && n !== this._popup || (n = this._popup, this._popup = null), n && this.removeLayer(n), this
            }
    });
    st.include({
        bindPopup: function(n, t)
        {
            if (n instanceof hr ? (l(n, t), this._popup = n, n._source = this) : ((!this._popup || t) && (this._popup = new hr(t, this)), this._popup.setContent(n)), !this._popupHandlersAdded)
            {
                this.on({
                    click: this._openPopup, keypress: this._onKeyPress, remove: this.closePopup, move: this._movePopup
                });
                this._popupHandlersAdded = !0
            }
            return this
        }, unbindPopup: function()
            {
                return this._popup && (this.off({
                        click: this._openPopup, keypress: this._onKeyPress, remove: this.closePopup, move: this._movePopup
                    }), this._popupHandlersAdded = !1, this._popup = null), this
            }, openPopup: function(n, t)
            {
                return this._popup && this._map && (t = this._popup._prepareOpen(this, n, t), this._map.openPopup(this._popup, t)), this
            }, closePopup: function()
            {
                return this._popup && this._popup._close(), this
            }, togglePopup: function(n)
            {
                return this._popup && (this._popup._map ? this.closePopup() : this.openPopup(n)), this
            }, isPopupOpen: function()
            {
                return this._popup ? this._popup.isOpen() : !1
            }, setPopupContent: function(n)
            {
                return this._popup && this._popup.setContent(n), this
            }, getPopup: function()
            {
                return this._popup
            }, _openPopup: function(n)
            {
                var t = n.layer || n.target;
                if (this._popup && this._map)
                {
                    if (bt(n), t instanceof ii)
                    {
                        this.openPopup(n.layer || n.target, n.latlng);
                        return
                    }
                    this._map.hasLayer(this._popup) && this._popup._source === t ? this.closePopup() : this.openPopup(t, n.latlng)
                }
            }, _movePopup: function(n)
            {
                this._popup.setLatLng(n.latlng)
            }, _onKeyPress: function(n)
            {
                n.originalEvent.keyCode === 13 && this._openPopup(n)
            }
    });
    vi = ri.extend({
        options: {
            pane: "tooltipPane", offset: [0, 0], direction: "auto", permanent: !1, sticky: !1, interactive: !1, opacity: .9
        }, onAdd: function(n)
            {
                ri.prototype.onAdd.call(this, n);
                this.setOpacity(this.options.opacity);
                n.fire("tooltipopen", {tooltip: this});
                this._source && this._source.fire("tooltipopen", {tooltip: this}, !0)
            }, onRemove: function(n)
            {
                ri.prototype.onRemove.call(this, n);
                n.fire("tooltipclose", {tooltip: this});
                this._source && this._source.fire("tooltipclose", {tooltip: this}, !0)
            }, getEvents: function()
            {
                var n = ri.prototype.getEvents.call(this);
                return pt && !this.options.permanent && (n.preclick = this._close), n
            }, _close: function()
            {
                this._map && this._map.closeTooltip(this)
            }, _initLayout: function()
            {
                var n = "leaflet-tooltip " + (this.options.className || "") + " leaflet-zoom-" + (this._zoomAnimated ? "animated" : "hide");
                this._contentNode = this._container = e("div", n)
            }, _updateLayout: function(){}, _adjustPan: function(){}, _setPosition: function(n)
            {
                var h = this._map,
                    u = this._container,
                    c = h.latLngToContainerPoint(h.getCenter()),
                    l = h.layerPointToContainerPoint(n),
                    f = this.options.direction,
                    o = u.offsetWidth,
                    s = u.offsetHeight,
                    t = r(this.options.offset),
                    e = this._getAnchor();
                f === "top" ? n = n.add(r(-o / 2 + t.x, -s + t.y + e.y, !0)) : f === "bottom" ? n = n.subtract(r(o / 2 - t.x, -t.y, !0)) : f === "center" ? n = n.subtract(r(o / 2 + t.x, s / 2 - e.y + t.y, !0)) : f === "right" || f === "auto" && l.x < c.x ? (f = "right", n = n.add(r(t.x + e.x, e.y - s / 2 + t.y, !0))) : (f = "left", n = n.subtract(r(o + e.x - t.x, s / 2 - e.y - t.y, !0)));
                p(u, "leaflet-tooltip-right");
                p(u, "leaflet-tooltip-left");
                p(u, "leaflet-tooltip-top");
                p(u, "leaflet-tooltip-bottom");
                i(u, "leaflet-tooltip-" + f);
                b(u, n)
            }, _updatePosition: function()
            {
                var n = this._map.latLngToLayerPoint(this._latlng);
                this._setPosition(n)
            }, setOpacity: function(n)
            {
                this.options.opacity = n;
                this._container && ut(this._container, n)
            }, _animateZoom: function(n)
            {
                var t = this._map._latLngToNewLayerPoint(this._latlng, n.zoom, n.center);
                this._setPosition(t)
            }, _getAnchor: function()
            {
                return r(this._source && this._source._getTooltipAnchor && !this.options.sticky ? this._source._getTooltipAnchor() : [0, 0])
            }
    });
    cc = function(n, t)
    {
        return new vi(n, t)
    };
    f.include({
        openTooltip: function(n, t, i)
        {
            return (n instanceof vi || (n = new vi(i).setContent(n)), t && n.setLatLng(t), this.hasLayer(n)) ? this : this.addLayer(n)
        }, closeTooltip: function(n)
            {
                return n && this.removeLayer(n), this
            }
    });
    st.include({
        bindTooltip: function(n, t)
        {
            return n instanceof vi ? (l(n, t), this._tooltip = n, n._source = this) : ((!this._tooltip || t) && (this._tooltip = new vi(t, this)), this._tooltip.setContent(n)), this._initTooltipInteractions(), this._tooltip.options.permanent && this._map && this._map.hasLayer(this) && this.openTooltip(), this
        }, unbindTooltip: function()
            {
                return this._tooltip && (this._initTooltipInteractions(!0), this.closeTooltip(), this._tooltip = null), this
            }, _initTooltipInteractions: function(n)
            {
                if (n || !this._tooltipHandlersAdded)
                {
                    var i = n ? "off" : "on",
                        t = {
                            remove: this.closeTooltip, move: this._moveTooltip
                        };
                    this._tooltip.options.permanent ? t.add = this._openTooltip : (t.mouseover = this._openTooltip, t.mouseout = this.closeTooltip, this._tooltip.options.sticky && (t.mousemove = this._moveTooltip), pt && (t.click = this._openTooltip));
                    this[i](t);
                    this._tooltipHandlersAdded = !n
                }
            }, openTooltip: function(n, t)
            {
                return this._tooltip && this._map && (t = this._tooltip._prepareOpen(this, n, t), this._map.openTooltip(this._tooltip, t), this._tooltip.options.interactive && this._tooltip._container && (i(this._tooltip._container, "leaflet-clickable"), this.addInteractiveTarget(this._tooltip._container))), this
            }, closeTooltip: function()
            {
                return this._tooltip && (this._tooltip._close(), this._tooltip.options.interactive && this._tooltip._container && (p(this._tooltip._container, "leaflet-clickable"), this.removeInteractiveTarget(this._tooltip._container))), this
            }, toggleTooltip: function(n)
            {
                return this._tooltip && (this._tooltip._map ? this.closeTooltip() : this.openTooltip(n)), this
            }, isTooltipOpen: function()
            {
                return this._tooltip.isOpen()
            }, setTooltipContent: function(n)
            {
                return this._tooltip && this._tooltip.setContent(n), this
            }, getTooltip: function()
            {
                return this._tooltip
            }, _openTooltip: function(n)
            {
                var t = n.layer || n.target;
                this._tooltip && this._map && this.openTooltip(t, this._tooltip.options.sticky ? n.latlng : undefined)
            }, _moveTooltip: function(n)
            {
                var t = n.latlng,
                    i,
                    r;
                this._tooltip.options.sticky && n.originalEvent && (i = this._map.mouseEventToContainerPoint(n.originalEvent), r = this._map.containerPointToLayerPoint(i), t = this._map.layerPointToLatLng(r));
                this._tooltip.setLatLng(t)
            }
    });
    po = or.extend({
        options: {
            iconSize: [12, 12], html: !1, bgPos: null, className: "leaflet-div-icon"
        }, createIcon: function(n)
            {
                var t = n && n.tagName === "DIV" ? n : document.createElement("div"),
                    i = this.options,
                    u;
                return i.html instanceof Element ? (pu(t), t.appendChild(i.html)) : t.innerHTML = i.html !== !1 ? i.html : "", i.bgPos && (u = r(i.bgPos), t.style.backgroundPosition = -u.x + "px " + -u.y + "px"), this._setIconStyles(t, "icon"), t
            }, createShadow: function()
            {
                return null
            }
    });
    or.Default = ru;
    cr = st.extend({
        options: {
            tileSize: 256, opacity: 1, updateWhenIdle: di, updateWhenZooming: !0, updateInterval: 200, zIndex: 1, bounds: null, minZoom: 0, maxZoom: undefined, maxNativeZoom: undefined, minNativeZoom: undefined, noWrap: !1, pane: "tilePane", className: "", keepBuffer: 2
        }, initialize: function(n)
            {
                l(this, n)
            }, onAdd: function()
            {
                this._initContainer();
                this._levels = {};
                this._tiles = {};
                this._resetView();
                this._update()
            }, beforeAdd: function(n)
            {
                n._addZoomLimit(this)
            }, onRemove: function(n)
            {
                this._removeAllTiles();
                v(this._container);
                n._removeZoomLimit(this);
                this._container = null;
                this._tileZoom = undefined
            }, bringToFront: function()
            {
                return this._map && (tr(this._container), this._setAutoZIndex(Math.max)), this
            }, bringToBack: function()
            {
                return this._map && (ir(this._container), this._setAutoZIndex(Math.min)), this
            }, getContainer: function()
            {
                return this._container
            }, setOpacity: function(n)
            {
                return this.options.opacity = n, this._updateOpacity(), this
            }, setZIndex: function(n)
            {
                return this.options.zIndex = n, this._updateZIndex(), this
            }, isLoading: function()
            {
                return this._loading
            }, redraw: function()
            {
                return this._map && (this._removeAllTiles(), this._update()), this
            }, getEvents: function()
            {
                var n = {
                        viewprereset: this._invalidateAll, viewreset: this._resetView, zoom: this._resetView, moveend: this._onMoveEnd
                    };
                return this.options.updateWhenIdle || (this._onMove || (this._onMove = af(this._onMoveEnd, this.options.updateInterval, this)), n.move = this._onMove), this._zoomAnimated && (n.zoomanim = this._animateZoom), n
            }, createTile: function()
            {
                return document.createElement("div")
            }, getTileSize: function()
            {
                var n = this.options.tileSize;
                return n instanceof t ? n : new t(n, n)
            }, _updateZIndex: function()
            {
                this._container && this.options.zIndex !== undefined && this.options.zIndex !== null && (this._container.style.zIndex = this.options.zIndex)
            }, _setAutoZIndex: function(n)
            {
                for (var r = this.getPane().children, t = -n(-Infinity, Infinity), i = 0, f = r.length, u; i < f; i++)
                    u = r[i].style.zIndex,
                    r[i] !== this._container && u && (t = n(t, +u));
                isFinite(t) && (this.options.zIndex = t + n(-1, 1), this._updateZIndex())
            }, _updateOpacity: function()
            {
                var u,
                    n,
                    t;
                if (this._map && !bi)
                {
                    ut(this._container, this.options.opacity);
                    var f = +new Date,
                        i = !1,
                        r = !1;
                    for (u in this._tiles)
                        (n = this._tiles[u], n.current && n.loaded) && (t = Math.min(1, (f - n.loaded) / 200), ut(n.el, t), t < 1 ? i = !0 : (n.active ? r = !0 : this._onOpaqueTile(n), n.active = !0));
                    r && !this._noPrune && this._pruneTiles();
                    i && (nt(this._fadeFrame), this._fadeFrame = g(this._updateOpacity, this))
                }
            }, _onOpaqueTile: k, _initContainer: function()
            {
                this._container || (this._container = e("div", "leaflet-layer " + (this.options.className || "")), this._updateZIndex(), this.options.opacity < 1 && this._updateOpacity(), this.getPane().appendChild(this._container))
            }, _updateLevels: function()
            {
                var i = this._tileZoom,
                    u = this.options.maxZoom,
                    t,
                    n,
                    r;
                if (i === undefined)
                    return undefined;
                for (t in this._levels)
                    this._levels[t].el.children.length || t === i ? (this._levels[t].el.style.zIndex = u - Math.abs(i - t), this._onUpdateLevel(t)) : (v(this._levels[t].el), this._removeTilesAtZoom(t), this._onRemoveLevel(t), delete this._levels[t]);
                return n = this._levels[i], r = this._map, n || (n = this._levels[i] = {}, n.el = e("div", "leaflet-tile-container leaflet-zoom-animated", this._container), n.el.style.zIndex = u, n.origin = r.project(r.unproject(r.getPixelOrigin()), i).round(), n.zoom = i, this._setZoomTransform(n, r.getCenter(), r.getZoom()), k(n.el.offsetWidth), this._onCreateLevel(n)), this._level = n, n
            }, _onUpdateLevel: k, _onRemoveLevel: k, _onCreateLevel: k, _pruneTiles: function()
            {
                var t,
                    i,
                    r,
                    n;
                if (this._map)
                {
                    if (r = this._map.getZoom(), r > this.options.maxZoom || r < this.options.minZoom)
                    {
                        this._removeAllTiles();
                        return
                    }
                    for (t in this._tiles)
                        i = this._tiles[t],
                        i.retain = i.current;
                    for (t in this._tiles)
                        i = this._tiles[t],
                        i.current && !i.active && (n = i.coords, this._retainParent(n.x, n.y, n.z, n.z - 5) || this._retainChildren(n.x, n.y, n.z, n.z + 2));
                    for (t in this._tiles)
                        this._tiles[t].retain || this._removeTile(t)
                }
            }, _removeTilesAtZoom: function(n)
            {
                for (var t in this._tiles)
                    this._tiles[t].coords.z === n && this._removeTile(t)
            }, _removeAllTiles: function()
            {
                for (var n in this._tiles)
                    this._removeTile(n)
            }, _invalidateAll: function()
            {
                for (var n in this._levels)
                    v(this._levels[n].el),
                    this._onRemoveLevel(n),
                    delete this._levels[n];
                this._removeAllTiles();
                this._tileZoom = undefined
            }, _retainParent: function(n, i, r, u)
            {
                var o = Math.floor(n / 2),
                    s = Math.floor(i / 2),
                    e = r - 1,
                    h = new t(+o, +s),
                    c,
                    f;
                return (h.z = +e, c = this._tileCoordsToKey(h), f = this._tiles[c], f && f.active) ? (f.retain = !0, !0) : (f && f.loaded && (f.retain = !0), e > u) ? this._retainParent(o, s, e, u) : !1
            }, _retainChildren: function(n, i, r, u)
            {
                for (var o, s, h, f, e = 2 * n; e < 2 * n + 2; e++)
                    for (o = 2 * i; o < 2 * i + 2; o++)
                    {
                        if (s = new t(e, o), s.z = r + 1, h = this._tileCoordsToKey(s), f = this._tiles[h], f && f.active)
                        {
                            f.retain = !0;
                            continue
                        }
                        else
                            f && f.loaded && (f.retain = !0);
                        r + 1 < u && this._retainChildren(e, o, r + 1, u)
                    }
            }, _resetView: function(n)
            {
                var t = n && (n.pinch || n.flyTo);
                this._setView(this._map.getCenter(), this._map.getZoom(), t, t)
            }, _animateZoom: function(n)
            {
                this._setView(n.center, n.zoom, !0, n.noUpdate)
            }, _clampZoom: function(n)
            {
                var t = this.options;
                return undefined !== t.minNativeZoom && n < t.minNativeZoom ? t.minNativeZoom : undefined !== t.maxNativeZoom && t.maxNativeZoom < n ? t.maxNativeZoom : n
            }, _setView: function(n, t, i, r)
            {
                var u = this._clampZoom(Math.round(t)),
                    f;
                (this.options.maxZoom !== undefined && u > this.options.maxZoom || this.options.minZoom !== undefined && u < this.options.minZoom) && (u = undefined);
                f = this.options.updateWhenZooming && u !== this._tileZoom;
                (!r || f) && (this._tileZoom = u, this._abortLoading && this._abortLoading(), this._updateLevels(), this._resetGrid(), u !== undefined && this._update(n), i || this._pruneTiles(), this._noPrune = !!i);
                this._setZoomTransforms(n, t)
            }, _setZoomTransforms: function(n, t)
            {
                for (var i in this._levels)
                    this._setZoomTransform(this._levels[i], n, t)
            }, _setZoomTransform: function(n, t, i)
            {
                var r = this._map.getZoomScale(i, n.zoom),
                    u = n.origin.multiplyBy(r).subtract(this._map._getNewPixelOrigin(t, i)).round();
                rt ? si(n.el, u, r) : b(n.el, u)
            }, _resetGrid: function()
            {
                var t = this._map,
                    n = t.options.crs,
                    i = this._tileSize = this.getTileSize(),
                    r = this._tileZoom,
                    u = this._map.getPixelWorldBounds(this._tileZoom);
                u && (this._globalTileRange = this._pxBoundsToTileRange(u));
                this._wrapX = n.wrapLng && !this.options.noWrap && [Math.floor(t.project([0, n.wrapLng[0]], r).x / i.x), Math.ceil(t.project([0, n.wrapLng[1]], r).x / i.y)];
                this._wrapY = n.wrapLat && !this.options.noWrap && [Math.floor(t.project([n.wrapLat[0], 0], r).y / i.x), Math.ceil(t.project([n.wrapLat[1], 0], r).y / i.y)]
            }, _onMoveEnd: function()
            {
                this._map && !this._map._animatingZoom && this._update()
            }, _getTiledPixelBounds: function(n)
            {
                var t = this._map,
                    u = t._animatingZoom ? Math.max(t._animateToZoom, t.getZoom()) : t.getZoom(),
                    f = t.getZoomScale(u, this._tileZoom),
                    i = t.project(n, this._tileZoom).floor(),
                    r = t.getSize().divideBy(f * 2);
                return new a(i.subtract(r), i.add(r))
            }, _update: function(n)
            {
                var h = this._map,
                    c,
                    l,
                    o,
                    s,
                    r,
                    f,
                    v,
                    y;
                if (h && (c = this._clampZoom(h.getZoom()), n === undefined && (n = h.getCenter()), this._tileZoom !== undefined))
                {
                    var w = this._getTiledPixelBounds(n),
                        i = this._pxBoundsToTileRange(w),
                        p = i.getCenter(),
                        u = [],
                        e = this.options.keepBuffer,
                        b = new a(i.getBottomLeft().subtract([e, -e]), i.getTopRight().add([e, -e]));
                    if (!(isFinite(i.min.x) && isFinite(i.min.y) && isFinite(i.max.x) && isFinite(i.max.y)))
                        throw new Error("Attempted to load an infinite number of tiles");
                    for (l in this._tiles)
                        o = this._tiles[l].coords,
                        o.z === this._tileZoom && b.contains(new t(o.x, o.y)) || (this._tiles[l].current = !1);
                    if (Math.abs(c - this._tileZoom) > 1)
                    {
                        this._setView(n, c);
                        return
                    }
                    for (s = i.min.y; s <= i.max.y; s++)
                        for (r = i.min.x; r <= i.max.x; r++)
                            (f = new t(r, s), f.z = this._tileZoom, this._isValidTile(f)) && (v = this._tiles[this._tileCoordsToKey(f)], v ? v.current = !0 : u.push(f));
                    if (u.sort(function(n, t)
                    {
                        return n.distanceTo(p) - t.distanceTo(p)
                    }), u.length !== 0)
                    {
                        for (this._loading || (this._loading = !0, this.fire("loading")), y = document.createDocumentFragment(), r = 0; r < u.length; r++)
                            this._addTile(u[r], y);
                        this._level.el.appendChild(y)
                    }
                }
            }, _isValidTile: function(n)
            {
                var i = this._map.options.crs,
                    t,
                    r;
                return !i.infinite && (t = this._globalTileRange, !i.wrapLng && (n.x < t.min.x || n.x > t.max.x) || !i.wrapLat && (n.y < t.min.y || n.y > t.max.y)) ? !1 : this.options.bounds ? (r = this._tileCoordsToBounds(n), d(this.options.bounds).overlaps(r)) : !0
            }, _keyToBounds: function(n)
            {
                return this._tileCoordsToBounds(this._keyToTileCoords(n))
            }, _tileCoordsToNwSe: function(n)
            {
                var t = this._map,
                    i = this.getTileSize(),
                    r = n.scaleBy(i),
                    u = r.add(i),
                    f = t.unproject(r, n.z),
                    e = t.unproject(u, n.z);
                return [f, e]
            }, _tileCoordsToBounds: function(n)
            {
                var i = this._tileCoordsToNwSe(n),
                    t = new it(i[0], i[1]);
                return this.options.noWrap || (t = this._map.wrapLatLngBounds(t)), t
            }, _tileCoordsToKey: function(n)
            {
                return n.x + ":" + n.y + ":" + n.z
            }, _keyToTileCoords: function(n)
            {
                var i = n.split(":"),
                    r = new t(+i[0], +i[1]);
                return r.z = +i[2], r
            }, _removeTile: function(n)
            {
                var t = this._tiles[n];
                t && (v(t.el), delete this._tiles[n], this.fire("tileunload", {
                        tile: t.el, coords: this._keyToTileCoords(n)
                    }))
            }, _initTile: function(n)
            {
                i(n, "leaflet-tile");
                var t = this.getTileSize();
                n.style.width = t.x + "px";
                n.style.height = t.y + "px";
                n.onselectstart = k;
                n.onmousemove = k;
                bi && this.options.opacity < 1 && ut(n, this.options.opacity);
                ki && !wr && (n.style.WebkitBackfaceVisibility = "hidden")
            }, _addTile: function(n, t)
            {
                var r = this._getTilePos(n),
                    u = this._tileCoordsToKey(n),
                    i = this.createTile(this._wrapCoords(n), c(this._tileReady, this, n));
                this._initTile(i);
                this.createTile.length < 2 && g(c(this._tileReady, this, n, null, i));
                b(i, r);
                this._tiles[u] = {
                    el: i, coords: n, current: !0
                };
                t.appendChild(i);
                this.fire("tileloadstart", {
                    tile: i, coords: n
                })
            }, _tileReady: function(n, t, r)
            {
                t && this.fire("tileerror", {
                    error: t, tile: r, coords: n
                });
                var u = this._tileCoordsToKey(n);
                (r = this._tiles[u], r) && (r.loaded = +new Date, this._map._fadeAnimated ? (ut(r.el, 0), nt(this._fadeFrame), this._fadeFrame = g(this._updateOpacity, this)) : (r.active = !0, this._pruneTiles()), t || (i(r.el, "leaflet-tile-loaded"), this.fire("tileload", {
                        tile: r.el, coords: n
                    })), this._noTilesToLoad() && (this._loading = !1, this.fire("load"), bi || !this._map._fadeAnimated ? g(this._pruneTiles, this) : setTimeout(c(this._pruneTiles, this), 250)))
            }, _getTilePos: function(n)
            {
                return n.scaleBy(this.getTileSize()).subtract(this._level.origin)
            }, _wrapCoords: function(n)
            {
                var i = new t(this._wrapX ? ar(n.x, this._wrapX) : n.x, this._wrapY ? ar(n.y, this._wrapY) : n.y);
                return i.z = n.z, i
            }, _pxBoundsToTileRange: function(n)
            {
                var t = this.getTileSize();
                return new a(n.min.unscaleBy(t).floor(), n.max.unscaleBy(t).ceil().subtract([1, 1]))
            }, _noTilesToLoad: function()
            {
                for (var n in this._tiles)
                    if (!this._tiles[n].loaded)
                        return !1;
                return !0
            }
    });
    yi = cr.extend({
        options: {
            minZoom: 0, maxZoom: 18, subdomains: "abc", errorTileUrl: "", zoomOffset: 0, tms: !1, zoomReverse: !1, detectRetina: !1, crossOrigin: !1
        }, initialize: function(n, t)
            {
                if (this._url = n, t = l(this, t), t.detectRetina && ei && t.maxZoom > 0 && (t.tileSize = Math.floor(t.tileSize / 2), t.zoomReverse ? (t.zoomOffset--, t.minZoom++) : (t.zoomOffset++, t.maxZoom--), t.minZoom = Math.max(0, t.minZoom)), typeof t.subdomains == "string" && (t.subdomains = t.subdomains.split("")), !ki)
                    this.on("tileunload", this._onTileRemove)
            }, setUrl: function(n, t)
            {
                return this._url === n && t === undefined && (t = !0), this._url = n, t || this.redraw(), this
            }, createTile: function(n, t)
            {
                var i = document.createElement("img");
                return u(i, "load", c(this._tileOnLoad, this, t, i)), u(i, "error", c(this._tileOnError, this, t, i)), (this.options.crossOrigin || this.options.crossOrigin === "") && (i.crossOrigin = this.options.crossOrigin === !0 ? "" : this.options.crossOrigin), i.alt = "", i.setAttribute("role", "presentation"), i.src = this.getTileUrl(n), i
            }, getTileUrl: function(n)
            {
                var t = {
                        r: ei ? "@2x" : "", s: this._getSubdomain(n), x: n.x, y: n.y, z: this._getZoomForUrl()
                    },
                    i;
                return this._map && !this._map.options.crs.infinite && (i = this._globalTileRange.max.y - n.y, this.options.tms && (t.y = i), t["-y"] = i), hs(this._url, s(t, this.options))
            }, _tileOnLoad: function(n, t)
            {
                bi ? setTimeout(c(n, this, null, t), 0) : n(null, t)
            }, _tileOnError: function(n, t, i)
            {
                var r = this.options.errorTileUrl;
                r && t.getAttribute("src") !== r && (t.src = r);
                n(i, t)
            }, _onTileRemove: function(n)
            {
                n.tile.onload = null
            }, _getZoomForUrl: function()
            {
                var n = this._tileZoom,
                    t = this.options.maxZoom,
                    i = this.options.zoomReverse,
                    r = this.options.zoomOffset;
                return i && (n = t - n), n + r
            }, _getSubdomain: function(n)
            {
                var t = Math.abs(n.x + n.y) % this.options.subdomains.length;
                return this.options.subdomains[t]
            }, _abortLoading: function()
            {
                var t,
                    n;
                for (t in this._tiles)
                    this._tiles[t].coords.z !== this._tileZoom && (n = this._tiles[t].el, n.onload = k, n.onerror = k, n.complete || (n.src = vr, v(n), delete this._tiles[t]))
            }, _removeTile: function(n)
            {
                var t = this._tiles[n];
                if (t)
                    return bs || t.el.setAttribute("src", vr), cr.prototype._removeTile.call(this, n)
            }, _tileReady: function(n, t, i)
            {
                if (this._map && (!i || i.getAttribute("src") !== vr))
                    return cr.prototype._tileReady.call(this, n, t, i)
            }
    });
    wo = yi.extend({
        defaultWmsParams: {
            service: "WMS", request: "GetMap", layers: "", styles: "", format: "image/jpeg", transparent: !1, version: "1.1.1"
        }, options: {
                crs: null, uppercase: !1
            }, initialize: function(n, t)
            {
                var i,
                    r,
                    u,
                    f;
                this._url = n;
                i = s({}, this.defaultWmsParams);
                for (r in t)
                    r in this.options || (i[r] = t[r]);
                t = l(this, t);
                u = t.detectRetina && ei ? 2 : 1;
                f = this.getTileSize();
                i.width = f.x * u;
                i.height = f.y * u;
                this.wmsParams = i
            }, onAdd: function(n)
            {
                this._crs = this.options.crs || n.options.crs;
                this._wmsVersion = parseFloat(this.wmsParams.version);
                var t = this._wmsVersion >= 1.3 ? "crs" : "srs";
                this.wmsParams[t] = this._crs.code;
                yi.prototype.onAdd.call(this, n)
            }, getTileUrl: function(n)
            {
                var r = this._tileCoordsToNwSe(n),
                    u = this._crs,
                    f = ct(u.project(r[0]), u.project(r[1])),
                    t = f.min,
                    i = f.max,
                    o = (this._wmsVersion >= 1.3 && this._crs === oc ? [t.y, t.x, i.y, i.x] : [t.x, t.y, i.x, i.y]).join(","),
                    e = yi.prototype.getTileUrl.call(this, n);
                return e + os(this.wmsParams, e, this.options.uppercase) + (this.options.uppercase ? "&BBOX=" : "&bbox=") + o
            }, setParams: function(n, t)
            {
                return s(this.wmsParams, n), t || this.redraw(), this
            }
    });
    yi.WMS = wo;
    lc.wms = ka;
    vt = st.extend({
        options: {
            padding: .1, tolerance: 0
        }, initialize: function(n)
            {
                l(this, n);
                o(this);
                this._layers = this._layers || {}
            }, onAdd: function()
            {
                this._container || (this._initContainer(), this._zoomAnimated && i(this._container, "leaflet-zoom-animated"));
                this.getPane().appendChild(this._container);
                this._update();
                this.on("update", this._updatePaths, this)
            }, onRemove: function()
            {
                this.off("update", this._updatePaths, this);
                this._destroyContainer()
            }, getEvents: function()
            {
                var n = {
                        viewreset: this._reset, zoom: this._onZoom, moveend: this._update, zoomend: this._onZoomEnd
                    };
                return this._zoomAnimated && (n.zoomanim = this._onAnimZoom), n
            }, _onAnimZoom: function(n)
            {
                this._updateTransform(n.center, n.zoom)
            }, _onZoom: function()
            {
                this._updateTransform(this._map.getCenter(), this._map.getZoom())
            }, _updateTransform: function(n, t)
            {
                var i = this._map.getZoomScale(t, this._zoom),
                    f = oi(this._container),
                    r = this._map.getSize().multiplyBy(.5 + this.options.padding),
                    e = this._map.project(this._center, t),
                    o = this._map.project(n, t),
                    s = o.subtract(e),
                    u = r.multiplyBy(-i).add(f).add(r).subtract(s);
                rt ? si(this._container, u, i) : b(this._container, u)
            }, _reset: function()
            {
                this._update();
                this._updateTransform(this._center, this._zoom);
                for (var n in this._layers)
                    this._layers[n]._reset()
            }, _onZoomEnd: function()
            {
                for (var n in this._layers)
                    this._layers[n]._project()
            }, _updatePaths: function()
            {
                for (var n in this._layers)
                    this._layers[n]._update()
            }, _update: function()
            {
                var n = this.options.padding,
                    t = this._map.getSize(),
                    i = this._map.containerPointToLayerPoint(t.multiplyBy(-n)).round();
                this._bounds = new a(i, i.add(t.multiplyBy(1 + n * 2)).round());
                this._center = this._map.getCenter();
                this._zoom = this._map.getZoom()
            }
    });
    bo = vt.extend({
        getEvents: function()
        {
            var n = vt.prototype.getEvents.call(this);
            return n.viewprereset = this._onViewPreReset, n
        }, _onViewPreReset: function()
            {
                this._postponeUpdatePaths = !0
            }, onAdd: function()
            {
                vt.prototype.onAdd.call(this);
                this._draw()
            }, _initContainer: function()
            {
                var n = this._container = document.createElement("canvas");
                u(n, "mousemove", af(this._onMouseMove, 32, this), this);
                u(n, "click dblclick mousedown mouseup contextmenu", this._onClick, this);
                u(n, "mouseout", this._handleMouseOut, this);
                this._ctx = n.getContext("2d")
            }, _destroyContainer: function()
            {
                nt(this._redrawRequest);
                delete this._ctx;
                v(this._container);
                w(this._container);
                delete this._container
            }, _updatePaths: function()
            {
                var n,
                    t;
                if (!this._postponeUpdatePaths)
                {
                    this._redrawBounds = null;
                    for (t in this._layers)
                        n = this._layers[t],
                        n._update();
                    this._redraw()
                }
            }, _update: function()
            {
                if (!this._map._animatingZoom || !this._bounds)
                {
                    vt.prototype._update.call(this);
                    var t = this._bounds,
                        n = this._container,
                        i = t.getSize(),
                        r = ei ? 2 : 1;
                    b(n, t.min);
                    n.width = r * i.x;
                    n.height = r * i.y;
                    n.style.width = i.x + "px";
                    n.style.height = i.y + "px";
                    ei && this._ctx.scale(2, 2);
                    this._ctx.translate(-t.min.x, -t.min.y);
                    this.fire("update")
                }
            }, _reset: function()
            {
                vt.prototype._reset.call(this);
                this._postponeUpdatePaths && (this._postponeUpdatePaths = !1, this._updatePaths())
            }, _initPath: function(n)
            {
                this._updateDashArray(n);
                this._layers[o(n)] = n;
                var t = n._order = {
                        layer: n, prev: this._drawLast, next: null
                    };
                this._drawLast && (this._drawLast.next = t);
                this._drawLast = t;
                this._drawFirst = this._drawFirst || this._drawLast
            }, _addPath: function(n)
            {
                this._requestRedraw(n)
            }, _removePath: function(n)
            {
                var r = n._order,
                    t = r.next,
                    i = r.prev;
                t ? t.prev = i : this._drawLast = i;
                i ? i.next = t : this._drawFirst = t;
                delete n._order;
                delete this._layers[o(n)];
                this._requestRedraw(n)
            }, _updatePath: function(n)
            {
                this._extendRedrawBounds(n);
                n._project();
                n._update();
                this._requestRedraw(n)
            }, _updateStyle: function(n)
            {
                this._updateDashArray(n);
                this._requestRedraw(n)
            }, _updateDashArray: function(n)
            {
                if (typeof n.options.dashArray == "string")
                {
                    for (var r = n.options.dashArray.split(/[, ]+/), u = [], i, t = 0; t < r.length; t++)
                    {
                        if (i = Number(r[t]), isNaN(i))
                            return;
                        u.push(i)
                    }
                    n.options._dashArray = u
                }
                else
                    n.options._dashArray = n.options.dashArray
            }, _requestRedraw: function(n)
            {
                this._map && (this._extendRedrawBounds(n), this._redrawRequest = this._redrawRequest || g(this._redraw, this))
            }, _extendRedrawBounds: function(n)
            {
                if (n._pxBounds)
                {
                    var t = (n.options.weight || 0) + 1;
                    this._redrawBounds = this._redrawBounds || new a;
                    this._redrawBounds.extend(n._pxBounds.min.subtract([t, t]));
                    this._redrawBounds.extend(n._pxBounds.max.add([t, t]))
                }
            }, _redraw: function()
            {
                this._redrawRequest = null;
                this._redrawBounds && (this._redrawBounds.min._floor(), this._redrawBounds.max._ceil());
                this._clear();
                this._draw();
                this._redrawBounds = null
            }, _clear: function()
            {
                var n = this._redrawBounds,
                    t;
                n ? (t = n.getSize(), this._ctx.clearRect(n.min.x, n.min.y, t.x, t.y)) : this._ctx.clearRect(0, 0, this._container.width, this._container.height)
            }, _draw: function()
            {
                var i,
                    n = this._redrawBounds,
                    r,
                    t;
                for (this._ctx.save(), n && (r = n.getSize(), this._ctx.beginPath(), this._ctx.rect(n.min.x, n.min.y, r.x, r.y), this._ctx.clip()), this._drawing = !0, t = this._drawFirst; t; t = t.next)
                    i = t.layer,
                    (!n || i._pxBounds && i._pxBounds.intersects(n)) && i._updatePath();
                this._drawing = !1;
                this._ctx.restore()
            }, _updatePoly: function(n, t)
            {
                if (this._drawing)
                {
                    var i,
                        r,
                        o,
                        f,
                        e = n._parts,
                        s = e.length,
                        u = this._ctx;
                    if (s)
                    {
                        for (u.beginPath(), i = 0; i < s; i++)
                        {
                            for (r = 0, o = e[i].length; r < o; r++)
                                f = e[i][r],
                                u[r ? "lineTo" : "moveTo"](f.x, f.y);
                            t && u.closePath()
                        }
                        this._fillStroke(u, n)
                    }
                }
            }, _updateCircle: function(n)
            {
                if (this._drawing && !n._empty())
                {
                    var u = n._point,
                        t = this._ctx,
                        r = Math.max(Math.round(n._radius), 1),
                        i = (Math.max(Math.round(n._radiusY), 1) || r) / r;
                    i !== 1 && (t.save(), t.scale(1, i));
                    t.beginPath();
                    t.arc(u.x, u.y / i, r, 0, Math.PI * 2, !1);
                    i !== 1 && t.restore();
                    this._fillStroke(t, n)
                }
            }, _fillStroke: function(n, t)
            {
                var i = t.options;
                i.fill && (n.globalAlpha = i.fillOpacity, n.fillStyle = i.fillColor || i.color, n.fill(i.fillRule || "evenodd"));
                i.stroke && i.weight !== 0 && (n.setLineDash && n.setLineDash(t.options && t.options._dashArray || []), n.globalAlpha = i.opacity, n.lineWidth = i.weight, n.strokeStyle = i.color, n.lineCap = i.lineCap, n.lineJoin = i.lineJoin, n.stroke())
            }, _onClick: function(n)
            {
                for (var u = this._map.mouseEventToLayerPoint(n), t, r, i = this._drawFirst; i; i = i.next)
                    t = i.layer,
                    t.options.interactive && t._containsPoint(u) && !this._map._draggableMoved(t) && (r = t);
                r && (to(n), this._fireEvent([r], n))
            }, _onMouseMove: function(n)
            {
                if (this._map && !this._map.dragging.moving() && !this._map._animatingZoom)
                {
                    var t = this._map.mouseEventToLayerPoint(n);
                    this._handleMouseHover(n, t)
                }
            }, _handleMouseOut: function(n)
            {
                var t = this._hoveredLayer;
                t && (p(this._container, "leaflet-interactive"), this._fireEvent([t], n, "mouseout"), this._hoveredLayer = null)
            }, _handleMouseHover: function(n, t)
            {
                for (var u, r, f = this._drawFirst; f; f = f.next)
                    u = f.layer,
                    u.options.interactive && u._containsPoint(t) && (r = u);
                r !== this._hoveredLayer && (this._handleMouseOut(n), r && (i(this._container, "leaflet-interactive"), this._fireEvent([r], n, "mouseover"), this._hoveredLayer = r));
                this._hoveredLayer && this._fireEvent([this._hoveredLayer], n)
            }, _fireEvent: function(n, t, i)
            {
                this._map._fireDOMEvent(t, i || t.type, n)
            }, _bringToFront: function(n)
            {
                var t = n._order,
                    i,
                    r;
                if (t)
                {
                    if (i = t.next, r = t.prev, i)
                        i.prev = r;
                    else
                        return;
                    r ? r.next = i : i && (this._drawFirst = i);
                    t.prev = this._drawLast;
                    this._drawLast.next = t;
                    t.next = null;
                    this._drawLast = t;
                    this._requestRedraw(n)
                }
            }, _bringToBack: function(n)
            {
                var t = n._order,
                    r,
                    i;
                if (t)
                {
                    if (r = t.next, i = t.prev, i)
                        i.next = r;
                    else
                        return;
                    r ? r.prev = i : i && (this._drawLast = i);
                    t.prev = null;
                    t.next = this._drawFirst;
                    this._drawFirst.prev = t;
                    this._drawFirst = t;
                    this._requestRedraw(n)
                }
            }
    });
    var eu = function()
        {
            try
            {
                return document.namespaces.add("lvml", "urn:schemas-microsoft-com:vml"), function(n)
                    {
                        return document.createElement("<lvml:" + n + ' class="lvml">')
                    }
            }
            catch(n)
            {
                return function(n)
                    {
                        return document.createElement("<" + n + ' xmlns="urn:schemas-microsoft.com:vml" class="lvml">')
                    }
            }
        }(),
        da = {
            _initContainer: function()
            {
                this._container = e("div", "leaflet-vml-container")
            }, _update: function()
                {
                    this._map._animatingZoom || (vt.prototype._update.call(this), this.fire("update"))
                }, _initPath: function(n)
                {
                    var t = n._container = eu("shape");
                    i(t, "leaflet-vml-shape " + (this.options.className || ""));
                    t.coordsize = "1 1";
                    n._path = eu("path");
                    t.appendChild(n._path);
                    this._updateStyle(n);
                    this._layers[o(n)] = n
                }, _addPath: function(n)
                {
                    var t = n._container;
                    this._container.appendChild(t);
                    n.options.interactive && n.addInteractiveTarget(t)
                }, _removePath: function(n)
                {
                    var t = n._container;
                    v(t);
                    n.removeInteractiveTarget(t);
                    delete this._layers[o(n)]
                }, _updateStyle: function(n)
                {
                    var i = n._stroke,
                        r = n._fill,
                        t = n.options,
                        u = n._container;
                    u.stroked = !!t.stroke;
                    u.filled = !!t.fill;
                    t.stroke ? (i || (i = n._stroke = eu("stroke")), u.appendChild(i), i.weight = t.weight + "px", i.color = t.color, i.opacity = t.opacity, i.dashStyle = t.dashArray ? ht(t.dashArray) ? t.dashArray.join(" ") : t.dashArray.replace(/( *, *)/g, " ") : "", i.endcap = t.lineCap.replace("butt", "flat"), i.joinstyle = t.lineJoin) : i && (u.removeChild(i), n._stroke = null);
                    t.fill ? (r || (r = n._fill = eu("fill")), u.appendChild(r), r.color = t.fillColor || t.color, r.opacity = t.fillOpacity) : r && (u.removeChild(r), n._fill = null)
                }, _updateCircle: function(n)
                {
                    var t = n._point.round(),
                        i = Math.round(n._radius),
                        r = Math.round(n._radiusY || i);
                    this._setPath(n, n._empty() ? "M0 0" : "AL " + t.x + "," + t.y + " " + i + "," + r + " 0,23592600")
                }, _setPath: function(n, t)
                {
                    n._path.v = t
                }, _bringToFront: function(n)
                {
                    tr(n._container)
                }, _bringToBack: function(n)
                {
                    ir(n._container)
                }
        },
        cf = au ? eu : ps,
        ou = vt.extend({
            getEvents: function()
            {
                var n = vt.prototype.getEvents.call(this);
                return n.zoomstart = this._onZoomStart, n
            }, _initContainer: function()
                {
                    this._container = cf("svg");
                    this._container.setAttribute("pointer-events", "none");
                    this._rootGroup = cf("g");
                    this._container.appendChild(this._rootGroup)
                }, _destroyContainer: function()
                {
                    v(this._container);
                    w(this._container);
                    delete this._container;
                    delete this._rootGroup;
                    delete this._svgSize
                }, _onZoomStart: function()
                {
                    this._update()
                }, _update: function()
                {
                    if (!this._map._animatingZoom || !this._bounds)
                    {
                        vt.prototype._update.call(this);
                        var t = this._bounds,
                            n = t.getSize(),
                            i = this._container;
                        this._svgSize && this._svgSize.equals(n) || (this._svgSize = n, i.setAttribute("width", n.x), i.setAttribute("height", n.y));
                        b(i, t.min);
                        i.setAttribute("viewBox", [t.min.x, t.min.y, n.x, n.y].join(" "));
                        this.fire("update")
                    }
                }, _initPath: function(n)
                {
                    var t = n._path = cf("path");
                    n.options.className && i(t, n.options.className);
                    n.options.interactive && i(t, "leaflet-interactive");
                    this._updateStyle(n);
                    this._layers[o(n)] = n
                }, _addPath: function(n)
                {
                    this._rootGroup || this._initContainer();
                    this._rootGroup.appendChild(n._path);
                    n.addInteractiveTarget(n._path)
                }, _removePath: function(n)
                {
                    v(n._path);
                    n.removeInteractiveTarget(n._path);
                    delete this._layers[o(n)]
                }, _updatePath: function(n)
                {
                    n._project();
                    n._update()
                }, _updateStyle: function(n)
                {
                    var t = n._path,
                        i = n.options;
                    t && (i.stroke ? (t.setAttribute("stroke", i.color), t.setAttribute("stroke-opacity", i.opacity), t.setAttribute("stroke-width", i.weight), t.setAttribute("stroke-linecap", i.lineCap), t.setAttribute("stroke-linejoin", i.lineJoin), i.dashArray ? t.setAttribute("stroke-dasharray", i.dashArray) : t.removeAttribute("stroke-dasharray"), i.dashOffset ? t.setAttribute("stroke-dashoffset", i.dashOffset) : t.removeAttribute("stroke-dashoffset")) : t.setAttribute("stroke", "none"), i.fill ? (t.setAttribute("fill", i.fillColor || i.color), t.setAttribute("fill-opacity", i.fillOpacity), t.setAttribute("fill-rule", i.fillRule || "evenodd")) : t.setAttribute("fill", "none"))
                }, _updatePoly: function(n, t)
                {
                    this._setPath(n, ws(n._parts, t))
                }, _updateCircle: function(n)
                {
                    var i = n._point,
                        t = Math.max(Math.round(n._radius), 1),
                        u = Math.max(Math.round(n._radiusY), 1) || t,
                        r = "a" + t + "," + u + " 0 1,0 ",
                        f = n._empty() ? "M0 0" : "M" + (i.x - t) + "," + i.y + r + t * 2 + ",0 " + r + -t * 2 + ",0 ";
                    this._setPath(n, f)
                }, _setPath: function(n, t)
                {
                    n._path.setAttribute("d", t)
                }, _bringToFront: function(n)
                {
                    tr(n._path)
                }, _bringToBack: function(n)
                {
                    ir(n._path)
                }
        });
    au && ou.include(da);
    f.include({
        getRenderer: function(n)
        {
            var t = n.options.renderer || this._getPaneRenderer(n.options.pane) || this.options.renderer || this._renderer;
            return t || (t = this._renderer = this._createRenderer()), this.hasLayer(t) || this.addLayer(t), t
        }, _getPaneRenderer: function(n)
            {
                if (n === "overlayPane" || n === undefined)
                    return !1;
                var t = this._paneRenderers[n];
                return t === undefined && (t = this._createRenderer({pane: n}), this._paneRenderers[n] = t), t
            }, _createRenderer: function(n)
            {
                return this.options.preferCanvas && ac(n) || vc(n)
            }
    });
    ko = ai.extend({
        initialize: function(n, t)
        {
            ai.prototype.initialize.call(this, this._boundsToLatLngs(n), t)
        }, setBounds: function(n)
            {
                return this.setLatLngs(this._boundsToLatLngs(n))
            }, _boundsToLatLngs: function(n)
            {
                return n = d(n), [n.getSouthWest(), n.getNorthWest(), n.getNorthEast(), n.getSouthEast()]
            }
    });
    ou.create = cf;
    ou.pointsToPath = ws;
    dt.geometryToLayer = lo;
    dt.coordsToLatLng = ao;
    dt.coordsToLatLngs = ff;
    dt.latLngToCoords = vo;
    dt.latLngsToCoords = ef;
    dt.getFeature = sr;
    dt.asFeature = of;
    f.mergeOptions({boxZoom: !0});
    go = at.extend({
        initialize: function(n)
        {
            this._map = n;
            this._container = n._container;
            this._pane = n._panes.overlayPane;
            this._resetStateTimeout = 0;
            n.on("unload", this._destroy, this)
        }, addHooks: function()
            {
                u(this._container, "mousedown", this._onMouseDown, this)
            }, removeHooks: function()
            {
                w(this._container, "mousedown", this._onMouseDown, this)
            }, moved: function()
            {
                return this._moved
            }, _destroy: function()
            {
                v(this._pane);
                delete this._pane
            }, _resetState: function()
            {
                this._resetStateTimeout = 0;
                this._moved = !1
            }, _clearDeferredResetState: function()
            {
                this._resetStateTimeout !== 0 && (clearTimeout(this._resetStateTimeout), this._resetStateTimeout = 0)
            }, _onMouseDown: function(n)
            {
                if (!n.shiftKey || n.which !== 1 && n.button !== 1)
                    return !1;
                this._clearDeferredResetState();
                this._resetState();
                gr();
                pe();
                this._startPoint = this._map.mouseEventToContainerPoint(n);
                u(document, {
                    contextmenu: bt, mousemove: this._onMouseMove, mouseup: this._onMouseUp, keydown: this._onKeyDown
                }, this)
            }, _onMouseMove: function(n)
            {
                this._moved || (this._moved = !0, this._box = e("div", "leaflet-zoom-box", this._container), i(this._container, "leaflet-crosshair"), this._map.fire("boxzoomstart"));
                this._point = this._map.mouseEventToContainerPoint(n);
                var t = new a(this._point, this._startPoint),
                    r = t.getSize();
                b(this._box, t.min);
                this._box.style.width = r.x + "px";
                this._box.style.height = r.y + "px"
            }, _finish: function()
            {
                this._moved && (v(this._box), p(this._container, "leaflet-crosshair"));
                nu();
                we();
                w(document, {
                    contextmenu: bt, mousemove: this._onMouseMove, mouseup: this._onMouseUp, keydown: this._onKeyDown
                }, this)
            }, _onMouseUp: function(n)
            {
                if ((n.which === 1 || n.button === 1) && (this._finish(), this._moved))
                {
                    this._clearDeferredResetState();
                    this._resetStateTimeout = setTimeout(c(this._resetState, this), 0);
                    var t = new it(this._map.containerPointToLatLng(this._startPoint), this._map.containerPointToLatLng(this._point));
                    this._map.fitBounds(t).fire("boxzoomend", {boxZoomBounds: t})
                }
            }, _onKeyDown: function(n)
            {
                n.keyCode === 27 && this._finish()
            }
    });
    f.addInitHook("addHandler", "boxZoom", go);
    f.mergeOptions({doubleClickZoom: !0});
    ns = at.extend({
        addHooks: function()
        {
            this._map.on("dblclick", this._onDoubleClick, this)
        }, removeHooks: function()
            {
                this._map.off("dblclick", this._onDoubleClick, this)
            }, _onDoubleClick: function(n)
            {
                var t = this._map,
                    i = t.getZoom(),
                    r = t.options.zoomDelta,
                    u = n.originalEvent.shiftKey ? i - r : i + r;
                t.options.doubleClickZoom === "center" ? t.setZoom(u) : t.setZoomAround(n.containerPoint, u)
            }
    });
    f.addInitHook("addHandler", "doubleClickZoom", ns);
    f.mergeOptions({
        dragging: !0, inertia: !wr, inertiaDeceleration: 3400, inertiaMaxSpeed: Infinity, easeLinearity: .2, worldCopyJump: !1, maxBoundsViscosity: 0
    });
    ts = at.extend({
        addHooks: function()
        {
            if (!this._draggable)
            {
                var n = this._map;
                this._draggable = new ci(n._mapPane, n._container);
                this._draggable.on({
                    dragstart: this._onDragStart, drag: this._onDrag, dragend: this._onDragEnd
                }, this);
                this._draggable.on("predrag", this._onPreDragLimit, this);
                if (n.options.worldCopyJump)
                {
                    this._draggable.on("predrag", this._onPreDragWrap, this);
                    n.on("zoomend", this._onZoomEnd, this);
                    n.whenReady(this._onZoomEnd, this)
                }
            }
            i(this._map._container, "leaflet-grab leaflet-touch-drag");
            this._draggable.enable();
            this._positions = [];
            this._times = []
        }, removeHooks: function()
            {
                p(this._map._container, "leaflet-grab");
                p(this._map._container, "leaflet-touch-drag");
                this._draggable.disable()
            }, moved: function()
            {
                return this._draggable && this._draggable._moved
            }, moving: function()
            {
                return this._draggable && this._draggable._moving
            }, _onDragStart: function()
            {
                var n = this._map,
                    t;
                n._stop();
                this._map.options.maxBounds && this._map.options.maxBoundsViscosity ? (t = d(this._map.options.maxBounds), this._offsetLimit = ct(this._map.latLngToContainerPoint(t.getNorthWest()).multiplyBy(-1), this._map.latLngToContainerPoint(t.getSouthEast()).multiplyBy(-1).add(this._map.getSize())), this._viscosity = Math.min(1, Math.max(0, this._map.options.maxBoundsViscosity))) : this._offsetLimit = null;
                n.fire("movestart").fire("dragstart");
                n.options.inertia && (this._positions = [], this._times = [])
            }, _onDrag: function(n)
            {
                if (this._map.options.inertia)
                {
                    var t = this._lastTime = +new Date,
                        i = this._lastPos = this._draggable._absPos || this._draggable._newPos;
                    this._positions.push(i);
                    this._times.push(t);
                    this._prunePositions(t)
                }
                this._map.fire("move", n).fire("drag", n)
            }, _prunePositions: function(n)
            {
                while (this._positions.length > 1 && n - this._times[0] > 50)
                    this._positions.shift(),
                    this._times.shift()
            }, _onZoomEnd: function()
            {
                var n = this._map.getSize().divideBy(2),
                    t = this._map.latLngToLayerPoint([0, 0]);
                this._initialWorldOffset = t.subtract(n).x;
                this._worldWidth = this._map.getPixelWorldBounds().getSize().x
            }, _viscousLimit: function(n, t)
            {
                return n - (n - t) * this._viscosity
            }, _onPreDragLimit: function()
            {
                if (this._viscosity && this._offsetLimit)
                {
                    var n = this._draggable._newPos.subtract(this._draggable._startPos),
                        t = this._offsetLimit;
                    n.x < t.min.x && (n.x = this._viscousLimit(n.x, t.min.x));
                    n.y < t.min.y && (n.y = this._viscousLimit(n.y, t.min.y));
                    n.x > t.max.x && (n.x = this._viscousLimit(n.x, t.max.x));
                    n.y > t.max.y && (n.y = this._viscousLimit(n.y, t.max.y));
                    this._draggable._newPos = this._draggable._startPos.add(n)
                }
            }, _onPreDragWrap: function()
            {
                var i = this._worldWidth,
                    t = Math.round(i / 2),
                    n = this._initialWorldOffset,
                    r = this._draggable._newPos.x,
                    u = (r - t + n) % i + t - n,
                    f = (r + t + n) % i - t - n,
                    e = Math.abs(u + n) < Math.abs(f + n) ? u : f;
                this._draggable._absPos = this._draggable._newPos.clone();
                this._draggable._newPos.x = e
            }, _onDragEnd: function(n)
            {
                var t = this._map,
                    r = t.options,
                    h = !r.inertia || this._times.length < 2;
                if (t.fire("dragend", n), h)
                    t.fire("moveend");
                else
                {
                    this._prunePositions(+new Date);
                    var c = this._lastPos.subtract(this._positions[0]),
                        l = (this._lastTime - this._times[0]) / 1e3,
                        u = r.easeLinearity,
                        f = c.multiplyBy(u / l),
                        e = f.distanceTo([0, 0]),
                        o = Math.min(r.inertiaMaxSpeed, e),
                        a = f.multiplyBy(o / e),
                        s = o / (r.inertiaDeceleration * u),
                        i = a.multiplyBy(-s / 2).round();
                    i.x || i.y ? (i = t._limitOffset(i, t.options.maxBounds), g(function()
                    {
                        t.panBy(i, {
                            duration: s, easeLinearity: u, noMoveStart: !0, animate: !0
                        })
                    })) : t.fire("moveend")
                }
            }
    });
    f.addInitHook("addHandler", "dragging", ts);
    f.mergeOptions({
        keyboard: !0, keyboardPanDelta: 80
    });
    is = at.extend({
        keyCodes: {
            left: [37], right: [39], down: [40], up: [38], zoomIn: [187, 107, 61, 171], zoomOut: [189, 109, 54, 173]
        }, initialize: function(n)
            {
                this._map = n;
                this._setPanDelta(n.options.keyboardPanDelta);
                this._setZoomDelta(n.options.zoomDelta)
            }, addHooks: function()
            {
                var n = this._map._container;
                n.tabIndex <= 0 && (n.tabIndex = "0");
                u(n, {
                    focus: this._onFocus, blur: this._onBlur, mousedown: this._onMouseDown
                }, this);
                this._map.on({
                    focus: this._addHooks, blur: this._removeHooks
                }, this)
            }, removeHooks: function()
            {
                this._removeHooks();
                w(this._map._container, {
                    focus: this._onFocus, blur: this._onBlur, mousedown: this._onMouseDown
                }, this);
                this._map.off({
                    focus: this._addHooks, blur: this._removeHooks
                }, this)
            }, _onMouseDown: function()
            {
                if (!this._focused)
                {
                    var n = document.body,
                        t = document.documentElement,
                        i = n.scrollTop || t.scrollTop,
                        r = n.scrollLeft || t.scrollLeft;
                    this._map._container.focus();
                    window.scrollTo(r, i)
                }
            }, _onFocus: function()
            {
                this._focused = !0;
                this._map.fire("focus")
            }, _onBlur: function()
            {
                this._focused = !1;
                this._map.fire("blur")
            }, _setPanDelta: function(n)
            {
                for (var u = this._panKeys = {}, i = this.keyCodes, t = 0, r = i.left.length; t < r; t++)
                    u[i.left[t]] = [-1 * n, 0];
                for (t = 0, r = i.right.length; t < r; t++)
                    u[i.right[t]] = [n, 0];
                for (t = 0, r = i.down.length; t < r; t++)
                    u[i.down[t]] = [0, n];
                for (t = 0, r = i.up.length; t < r; t++)
                    u[i.up[t]] = [0, -1 * n]
            }, _setZoomDelta: function(n)
            {
                for (var u = this._zoomKeys = {}, i = this.keyCodes, t = 0, r = i.zoomIn.length; t < r; t++)
                    u[i.zoomIn[t]] = n;
                for (t = 0, r = i.zoomOut.length; t < r; t++)
                    u[i.zoomOut[t]] = -n
            }, _addHooks: function()
            {
                u(document, "keydown", this._onKeyDown, this)
            }, _removeHooks: function()
            {
                w(document, "keydown", this._onKeyDown, this)
            }, _onKeyDown: function(n)
            {
                if (!n.altKey && !n.ctrlKey && !n.metaKey)
                {
                    var i = n.keyCode,
                        t = this._map,
                        u;
                    if (i in this._panKeys)
                        t._panAnim && t._panAnim._inProgress || (u = this._panKeys[i], n.shiftKey && (u = r(u).multiplyBy(3)), t.panBy(u), t.options.maxBounds && t.panInsideBounds(t.options.maxBounds));
                    else if (i in this._zoomKeys)
                        t.setZoom(t.getZoom() + (n.shiftKey ? 3 : 1) * this._zoomKeys[i]);
                    else if (i === 27 && t._popup && t._popup.options.closeOnEscapeKey)
                        t.closePopup();
                    else
                        return;
                    bt(n)
                }
            }
    });
    f.addInitHook("addHandler", "keyboard", is);
    f.mergeOptions({
        scrollWheelZoom: !0, wheelDebounceTime: 40, wheelPxPerZoomLevel: 60
    });
    rs = at.extend({
        addHooks: function()
        {
            u(this._map._container, "mousewheel", this._onWheelScroll, this);
            this._delta = 0
        }, removeHooks: function()
            {
                w(this._map._container, "mousewheel", this._onWheelScroll, this)
            }, _onWheelScroll: function(n)
            {
                var i = yh(n),
                    r = this._map.options.wheelDebounceTime,
                    t;
                this._delta += i;
                this._lastMousePos = this._map.mouseEventToContainerPoint(n);
                this._startTime || (this._startTime = +new Date);
                t = Math.max(r - (+new Date - this._startTime), 0);
                clearTimeout(this._timer);
                this._timer = setTimeout(c(this._performZoom, this), t);
                bt(n)
            }, _performZoom: function()
            {
                var n = this._map,
                    t = n.getZoom(),
                    i = this._map.options.zoomSnap || 0;
                n._stop();
                var e = this._delta / (this._map.options.wheelPxPerZoomLevel * 4),
                    u = 4 * Math.log(2 / (1 + Math.exp(-Math.abs(e)))) / Math.LN2,
                    f = i ? Math.ceil(u / i) * i : u,
                    r = n._limitZoom(t + (this._delta > 0 ? f : -f)) - t;
                (this._delta = 0, this._startTime = null, r) && (n.options.scrollWheelZoom === "center" ? n.setZoom(t + r) : n.setZoomAround(this._lastMousePos, t + r))
            }
    });
    f.addInitHook("addHandler", "scrollWheelZoom", rs);
    f.mergeOptions({
        tap: !0, tapTolerance: 15
    });
    us = at.extend({
        addHooks: function()
        {
            u(this._map._container, "touchstart", this._onDown, this)
        }, removeHooks: function()
            {
                w(this._map._container, "touchstart", this._onDown, this)
            }, _onDown: function(n)
            {
                if (n.touches)
                {
                    if (et(n), this._fireClick = !0, n.touches.length > 1)
                    {
                        this._fireClick = !1;
                        clearTimeout(this._holdTimeout);
                        return
                    }
                    var r = n.touches[0],
                        f = r.target;
                    this._startPos = this._newPos = new t(r.clientX, r.clientY);
                    f.tagName && f.tagName.toLowerCase() === "a" && i(f, "leaflet-active");
                    this._holdTimeout = setTimeout(c(function()
                    {
                        this._isTapValid() && (this._fireClick = !1, this._onUp(), this._simulateEvent("contextmenu", r))
                    }, this), 1e3);
                    this._simulateEvent("mousedown", r);
                    u(document, {
                        touchmove: this._onMove, touchend: this._onUp
                    }, this)
                }
            }, _onUp: function(n)
            {
                if (clearTimeout(this._holdTimeout), w(document, {
                    touchmove: this._onMove, touchend: this._onUp
                }, this), this._fireClick && n && n.changedTouches)
                {
                    var i = n.changedTouches[0],
                        t = i.target;
                    t && t.tagName && t.tagName.toLowerCase() === "a" && p(t, "leaflet-active");
                    this._simulateEvent("mouseup", i);
                    this._isTapValid() && this._simulateEvent("click", i)
                }
            }, _isTapValid: function()
            {
                return this._newPos.distanceTo(this._startPos) <= this._map.options.tapTolerance
            }, _onMove: function(n)
            {
                var i = n.touches[0];
                this._newPos = new t(i.clientX, i.clientY);
                this._simulateEvent("mousemove", i)
            }, _simulateEvent: function(n, t)
            {
                var i = document.createEvent("MouseEvents");
                i._simulated = !0;
                t.target._simulatedClick = !0;
                i.initMouseEvent(n, !0, !0, window, 1, t.screenX, t.screenY, t.clientX, t.clientY, !1, !1, !1, !1, 0, null);
                t.target.dispatchEvent(i)
            }
    });
    pt && !lt && f.addInitHook("addHandler", "tap", us);
    f.mergeOptions({
        touchZoom: pt && !wr, bounceAtZoomLimits: !0
    });
    fs = at.extend({
        addHooks: function()
        {
            i(this._map._container, "leaflet-touch-zoom");
            u(this._map._container, "touchstart", this._onTouchStart, this)
        }, removeHooks: function()
            {
                p(this._map._container, "leaflet-touch-zoom");
                w(this._map._container, "touchstart", this._onTouchStart, this)
            }, _onTouchStart: function(n)
            {
                var t = this._map,
                    i,
                    r;
                !n.touches || n.touches.length !== 2 || t._animatingZoom || this._zooming || (i = t.mouseEventToContainerPoint(n.touches[0]), r = t.mouseEventToContainerPoint(n.touches[1]), this._centerPoint = t.getSize()._divideBy(2), this._startLatLng = t.containerPointToLatLng(this._centerPoint), t.options.touchZoom !== "center" && (this._pinchStartLatLng = t.containerPointToLatLng(i.add(r)._divideBy(2))), this._startDist = i.distanceTo(r), this._startZoom = t.getZoom(), this._moved = !1, this._zooming = !0, t._stop(), u(document, "touchmove", this._onTouchMove, this), u(document, "touchend", this._onTouchEnd, this), et(n))
            }, _onTouchMove: function(n)
            {
                var r,
                    e;
                if (n.touches && n.touches.length === 2 && this._zooming)
                {
                    var t = this._map,
                        u = t.mouseEventToContainerPoint(n.touches[0]),
                        f = t.mouseEventToContainerPoint(n.touches[1]),
                        i = u.distanceTo(f) / this._startDist;
                    if (this._zoom = t.getScaleZoom(i, this._startZoom), !t.options.bounceAtZoomLimits && (this._zoom < t.getMinZoom() && i < 1 || this._zoom > t.getMaxZoom() && i > 1) && (this._zoom = t._limitZoom(this._zoom)), t.options.touchZoom === "center")
                    {
                        if (this._center = this._startLatLng, i === 1)
                            return
                    }
                    else
                    {
                        if (r = u._add(f)._divideBy(2)._subtract(this._centerPoint), i === 1 && r.x === 0 && r.y === 0)
                            return;
                        this._center = t.unproject(t.project(this._pinchStartLatLng, this._zoom).subtract(r), this._zoom)
                    }
                    this._moved || (t._moveStart(!0, !1), this._moved = !0);
                    nt(this._animRequest);
                    e = c(t._move, t, this._center, this._zoom, {
                        pinch: !0, round: !1
                    });
                    this._animRequest = g(e, this, !0);
                    et(n)
                }
            }, _onTouchEnd: function()
            {
                if (!this._moved || !this._zooming)
                {
                    this._zooming = !1;
                    return
                }
                this._zooming = !1;
                nt(this._animRequest);
                w(document, "touchmove", this._onTouchMove);
                w(document, "touchend", this._onTouchEnd);
                this._map.options.zoomAnimation ? this._map._animateZoom(this._center, this._map._limitZoom(this._zoom), !0, this._map.options.zoomSnap) : this._map._resetView(this._center, this._map._limitZoom(this._zoom))
            }
    });
    f.addInitHook("addHandler", "touchZoom", fs);
    f.BoxZoom = go;
    f.DoubleClickZoom = ns;
    f.Drag = ts;
    f.Keyboard = is;
    f.ScrollWheelZoom = rs;
    f.Tap = us;
    f.TouchZoom = fs;
    Object.freeze = es;
    n.version = "1.5.1";
    n.Control = ot;
    n.control = ur;
    n.Browser = gc;
    n.Evented = wi;
    n.Mixin = pl;
    n.Util = as;
    n.Class = gt;
    n.Handler = at;
    n.extend = s;
    n.bind = c;
    n.stamp = o;
    n.setOptions = l;
    n.DomEvent = cl;
    n.DomUtil = lh;
    n.PosAnimation = ph;
    n.Draggable = ci;
    n.LineUtil = fc;
    n.PolyUtil = gl;
    n.Point = t;
    n.point = r;
    n.Bounds = a;
    n.bounds = ct;
    n.Transformation = df;
    n.transformation = yr;
    n.Projection = na;
    n.LatLng = h;
    n.latLng = y;
    n.LatLngBounds = it;
    n.latLngBounds = d;
    n.CRS = ni;
    n.GeoJSON = dt;
    n.geoJSON = sc;
    n.geoJson = la;
    n.Layer = st;
    n.LayerGroup = fr;
    n.layerGroup = ra;
    n.FeatureGroup = er;
    n.featureGroup = ua;
    n.ImageOverlay = hf;
    n.imageOverlay = aa;
    n.VideoOverlay = hc;
    n.videoOverlay = va;
    n.SVGOverlay = yo;
    n.svgOverlay = ya;
    n.DivOverlay = ri;
    n.Popup = hr;
    n.popup = pa;
    n.Tooltip = vi;
    n.tooltip = cc;
    n.Icon = or;
    n.icon = fa;
    n.DivIcon = po;
    n.divIcon = wa;
    n.Marker = uu;
    n.marker = ea;
    n.TileLayer = yi;
    n.tileLayer = lc;
    n.GridLayer = cr;
    n.gridLayer = ba;
    n.SVG = ou;
    n.svg = vc;
    n.Renderer = vt;
    n.Canvas = bo;
    n.canvas = ac;
    n.Path = ii;
    n.CircleMarker = fu;
    n.circleMarker = oa;
    n.Circle = uf;
    n.circle = sa;
    n.Polyline = kt;
    n.polyline = ha;
    n.Polygon = ai;
    n.polygon = ca;
    n.Rectangle = ko;
    n.rectangle = ga;
    n.Map = f;
    n.map = ll;
    n.MarkerDrag = co;
    yc = window.L;
    n.noConflict = function()
    {
        return window.L = yc, this
    };
    window.L = n
})
