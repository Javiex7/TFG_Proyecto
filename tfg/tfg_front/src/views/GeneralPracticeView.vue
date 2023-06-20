<template>
  <b-container style="padding: 1rem">
    <!-- Category quizzes -->
    <b-row style="margin-top: 1rem">
      <CategoryQuizzes :quizzes="quizzes" v-if="quizzes" />
      <b-container v-else>
        <p>No hay cuestionarios generales disponibles por el momento...</p>
        <b-button v-bind:href="'/'" variant="secondary">Volver</b-button>
      </b-container>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
import Constants from "@/constants";

import CategoryQuizzes from "../components/category_detail/CategoryQuizzes.vue";

export default {
  data() {
    return {
      quizzes: null,
    };
  },

  components: {
    CategoryQuizzes,
  },

  methods: {
    getGenericQuizzes() {
      const path = Constants.API_URL + "quizzes/getGenericQuizzes/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then((response) => {
          this.quizzes = response.data;
        })
        .catch((error) => {
          if (error.response && error.response.status == 401) {
            localStorage.clear();
            this.$router.push({ path: "/login", replace: true });
          }
        });
    },
  },

  created() {
    if (this.$store.state.isAuthenticated) {
      this.getGenericQuizzes(this.packId);
    } else {
      localStorage.clear();
      this.$router.push({ path: "/login", replace: true });
    }
  },
};
</script>
