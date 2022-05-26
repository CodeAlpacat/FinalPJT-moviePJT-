import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'
import '@fortawesome/fontawesome-free/js/all.js'
import 'animate.css';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false

import AOS from 'aos';
import "aos/dist/aos.css";

new Vue({
  store,
  router,
  vuetify,
  created() {
    AOS.init();
},
  render: h => h(App)
}).$mount('#app')
