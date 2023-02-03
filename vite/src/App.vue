<template>
  <div id="container">
    <a href="https://vitejs.dev" target="_blank">
      <img src="./assets/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
    <hello-world msg="Vite + Vue" />
  </div>
</template>

<script>
import favicon from "@/assets/vite.svg";

import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
  created() {
    document.getElementById("favicon").href = favicon;
  },
};
</script>

<style scoped>
#container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
