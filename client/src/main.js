/**
 * Main app dep
*/
import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router';
import axios from 'axios';
// import VueAxios from 'vue-axios'

/**
 * Ohter specific dep
*/
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';

/**
 * Import relative app
*/
import Contacts from './components/Contacts.vue';

Vue.config.productionTip = false
Vue.use(BootstrapVue, Router, axios);
// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'

/**
 * Note that this route will be not used for now
 * Placed here just for refference and future update
*/
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Contacts',
      component: Contacts,
    },
  ],
});

new Vue({
  Router,
  render: h => h(App)
}).$mount('#app')