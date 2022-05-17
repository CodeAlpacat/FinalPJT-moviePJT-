<template>
  <div>
    <section>
      <span class="text" v-for="(n, idx) in helloWorld" :key="idx"
        >{{ n }}&nbsp;</span
      >
      <button class="text-center"></button>
    </section>
  </div>
</template>

<script>
import VueAnime from "vue-animejs";
import Vue from "vue";
Vue.use(VueAnime);

export default {
  name: "StartView",
  data() {
    return {
      helloWorld: "DORAITHON",
    };
  },
  mounted() {
    this.$anime({
      targets: ".text",
      width: "100%", // -> from '28px' to '100%',
      easing: "easeInOutQuad",
      direction: "alternate",
    });
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
section {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: rgb(225, 225, 225);
  overflow: hidden;
}
section .text {
  position: relative;
  font-size: 5em;
  text-align: center;
  color: rgb(27 45 71);
  -webkit-box-reflect: below -0.46em linear-gradient(transparent, #0004);
}
section .text span {
  position: relative;
}
</style>
