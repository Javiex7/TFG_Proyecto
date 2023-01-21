<template>
  <div class="container">
    <div class="row" style="margin-top: 2rem">
      <div class="row">
        <h2>Categorías!</h2>
      </div>

      <div class="row" style="margin-top: 2rem">
        <b-card-group deck>
          <label v-for="category in categories" :key="category.id">
            <p style="margin: 1rem">
              <b-card
                :title="category.title"
                img-src="https://demos.creative-tim.com/argon-dashboard-pro-bs4/assets/img/theme/img-1-1000x600.jpg"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem"
                class="mb-2"
              >
                <b-card-text :text="category.content"> </b-card-text>

                <b-button
                  v-bind:href="'/categories/' + category.id"
                  variant="primary"
                  >Acceder</b-button
                >
              </b-card>
            </p></label
          >
        </b-card-group>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      fields: [{ key: "title", label: "Título" }],
      categories: [],
    };
  },

  methods: {
    getCategories() {
      const path = "http://localhost:8000/api/v1.0/categories/";
      axios
        .get(path)
        .then((response) => {
          this.categories = response.data.results;
          console.log(this.categories);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getCategories();
  },
};
</script>
