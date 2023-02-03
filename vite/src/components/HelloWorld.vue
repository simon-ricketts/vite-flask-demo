<template>
  <div>
    <h1>{{ msg }}</h1>
    <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
    <div>
      The current time is:
      {{ currentTime ? currentTime : "undefined, press the button" }}
    </div>
    <button @click="fetchCurrentTime()">Get Time</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  props: {
    msg: { type: String, default: null },
  },
  data() {
    return {
      currentTime: null,
    };
  },
  methods: {
    fetchCurrentTime() {
      axios.get("/api/time/current").then((resp) => {
        this.currentTime = resp.data.current_time;
      });
    },
  },
};
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
