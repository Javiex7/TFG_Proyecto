<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "HomeView",

  components: {
    HelloWorld,
  },

  created() {
    const path = "http://localhost:8000/auth/users/me/";

    console.log("GET USER:", "Token " + localStorage.getItem("user_token"));

    axios
      .get(path, {
        headers: {
          Authorization: "Token " + localStorage.getItem("user_token"),
        },
      })
      .then((response) => {
        console.log("GET USER: ", response);
      })
      .catch((error) => {
        console.log(error.response.data);
      });
  },
};
</script>
