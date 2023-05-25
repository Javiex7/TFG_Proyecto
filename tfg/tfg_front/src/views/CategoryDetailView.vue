<template>
  <b-container style="padding: 1rem">
    <b-row style="margin-top: 1rem">
      <!-- Introduction text -->
      <b-col lg="7">
        <b-row>
          <h2 class="text-start">{{ categoryDetail.title }}</h2>
        </b-row>
        <b-row style="margin-top: 1rem">
          <p class="text-start" style="white-space: pre-wrap">
            {{ categoryDetail.content }}
          </p>
        </b-row>
      </b-col>

      <!-- Main image -->
      <b-col lg="5" align-self="center" style="margin-top: 1rem">
        <b-img
          :src="categoryDetail.image"
          rounded="pill"
          width="300rem"
          height="300rem"
          class="main-image"
        />
      </b-col>
    </b-row>

    <b-row style="margin-top: 4rem">
      <b-row>
        <h3 class="text-start">Cuestionarios</h3>
      </b-row>

      <!-- Category quizzes -->
      <b-card-group deck>
        <label v-for="quiz in categoryDetail.quizzes" :key="quiz.id">
          <p style="margin: 1.5rem">
            <b-card style="max-width: 20rem" border-variant="secondary">
              <b-card-title :text="quiz.name" tag="h4" class="text-start" />

              <b-card-text
                :text="quiz.description"
                tag="p"
                class="text-start"
              />

              <b-button v-bind:href="'/quizzes/' + quiz.id" variant="secondary"
                >Acceder
              </b-button>
            </b-card>
          </p>
        </label>
      </b-card-group>
    </b-row>

    <b-modal>Hello From My Modal!</b-modal>

    <b-row style="margin-top: 4rem">
      <b-row style="margin-bottom: 1rem">
        <h3 class="text-start">Material adicional</h3>
      </b-row>

      <b-row>
        <!-- Additional content -->
        <label v-for="file in categoryDetail.associated_files" :key="file.id">
          <p style="text-align: start">
            <a :href="serverURL + file.file" target="_blank">{{ file.name }}</a>
          </p>
        </label>
      </b-row>
    </b-row>
  </b-container>
</template>

<style scoped>
.main-image {
  border: 2px solid #555;
}
</style>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data() {
    return {
      categoryDetail: {},
      serverURL: Constants.BASE_URL,
    };
  },

  methods: {
    getCategoryDetail() {
      const path =
        Constants.API_URL +
        "categories/" +
        parseInt(this.$route.params.categoryId) +
        "/";

      axios
        .get(path)
        .then((response) => {
          this.categoryDetail = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getCategoryDetail();
  },
};
</script>
