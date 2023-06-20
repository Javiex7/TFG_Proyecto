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

    <!-- Category quizzes -->
    <b-row style="margin-top: 4rem">
      <CategoryQuizzes :quizzes="categoryDetail.quizzes" />
    </b-row>

    <!-- Point packs -->
    <b-row style="margin-top: 4rem">
      <b-row style="margin-bottom: 1rem">
        <h3 class="text-start">Canjear puntos <i class="bi bi-stars"></i></h3>
      </b-row>

      <b-card-group deck>
        <label v-for="pack in categoryDetail.associated_packs" :key="pack.id">
          <p style="margin: 1.5rem">
            <b-card
              no-body
              class="overflow-hidden"
              style="max-width: 18rem"
              border-variant="secondary"
            >
              <b-row no-gutters align-v="center">
                <b-col cols="6">
                  <b-card-img :src="pack.img" class="rounded-0"></b-card-img>
                </b-col>
                <b-col cols="6">
                  <b-card-body :title="pack.name" class="text-center">
                    <b-button
                      v-bind:href="'/packs/' + pack.id"
                      variant="primary"
                      >Acceder <i class="bi bi-bag-check"></i>
                    </b-button>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </p>
        </label>
      </b-card-group>
    </b-row>

    <!-- Additional content -->
    <b-row style="margin-top: 4rem; margin-bottom: 3rem">
      <b-row style="margin-bottom: 1rem">
        <h3 class="text-start">
          Material adicional <i class="bi bi-file-earmark-pdf"></i>
        </h3>
      </b-row>

      <b-row>
        <label v-for="file in categoryDetail.associated_files" :key="file.id">
          <p style="text-align: start">
            <a class="custom-a" :href="serverURL + file.file" target="_blank">{{
              file.name
            }}</a>
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

import CategoryQuizzes from "../components/category_detail/CategoryQuizzes.vue";

export default {
  data() {
    return {
      categoryDetail: {},
      serverURL: Constants.BASE_URL,
    };
  },

  components: {
    CategoryQuizzes,
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

          if (this.categoryDetail.associated_packs) {
            let local_imgs = [];
            this.categoryDetail.associated_packs.forEach(function (pack) {
              if (local_imgs.length === 0) {
                local_imgs = Array.from(
                  Array(Constants.POINTS_PACKS_IMG_NUMBER).keys()
                );
              }

              let number =
                local_imgs[Math.floor(Math.random() * local_imgs.length)];

              const index = local_imgs.indexOf(number);
              if (index > -1) {
                local_imgs.splice(index, 1);
              }

              let img = number + 1 + ".png";
              var image = require.context("@/assets/pack_imgs/");
              pack.img = image("./" + img);
            });
          }
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
