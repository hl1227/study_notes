import Vue from 'vue'
import Router from 'vue-router'

import ViewUI from 'view-design';
import ElementUI from 'element-ui';

import 'view-design/dist/styles/iview.css';
import iview_xxx from './view/Iview_xxx';
import iview_yyy from './view/Iview_yyy';

import 'element-ui/lib/theme-chalk/index.css';
import elm_xxx from './view/Elm_xxx';
import elm_yyy from './view/Elm_yyy';

Vue.use(ViewUI);
Vue.use(ElementUI);

Vue.use(Router)

const router = new Router({
    routes: [
      {
        path: '/elm_login',
        name: 'elm_login',
        component: elm_xxx
      },
      {
        path: '/elm_index',
        name: 'elm_index',
        component: elm_yyy
      },
      {
        path: '/iview_login',
        name: 'iview_login',
        component: iview_xxx
      },
      {
        path: '/iview_index',
        name: 'iview_index',
        component: iview_yyy
      },
    ]
  })

  export default router
