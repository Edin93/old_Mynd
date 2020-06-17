import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _1ea6e30e = () => interopDefault(import('../pages/post/_id.vue' /* webpackChunkName: "pages/post/_id" */))
const _65444ed8 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))
const _5e8aa68c = () => interopDefault(import('../pages/_username/index.vue' /* webpackChunkName: "pages/_username/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/post/:id?",
    component: _1ea6e30e,
    name: "post-id"
  }, {
    path: "/",
    component: _65444ed8,
    name: "index"
  }, {
    path: "/:username",
    component: _5e8aa68c,
    name: "username"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
