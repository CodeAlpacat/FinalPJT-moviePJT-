import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Carousel3d from 'vue-carousel-3d';

Vue.use(Carousel3d)
Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'md' || 'fa'
  }
});
