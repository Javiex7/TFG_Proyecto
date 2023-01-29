<template>
  <div>PERFIL DE USUARIO</div>
  <nav>
    <p><router-link to="/login"> Login </router-link></p>
  </nav>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "HomeView",
  data: function () {
    return {
      user: null,
    };
  },
  updated() {
    const path = "http://localhost:8000/auth/users/me/";

    if (this.$store.state.isAuthenticated) {
      axios
        .get(path, {
          headers: {
            Authorization: "Token " + localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.user = response.data;
          console.log(this.user);
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    }
  },
};
</script>

<style scoped>
h5 {
  margin: 20px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}
</style>
