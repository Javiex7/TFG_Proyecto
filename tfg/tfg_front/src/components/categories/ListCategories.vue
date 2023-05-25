<template>
  <!-- Categories display -->
  <b-card-group deck>
    <label v-for="category in categories" :key="category.id">
      <p style="margin: 1.5rem">
        <b-card
          :img-alt="category.title"
          :img-src="category.image"
          img-height="175rem"
          img-top
          style="max-width: 20rem"
          border-variant="secondary"
        >
          <b-card-title :text="category.title" tag="h3" class="text-start" />

          <b-card-text
            :text="category.short_description"
            tag="p"
            class="text-start"
          />

          <b-button v-bind:href="'/categories/' + category.id" variant="primary"
            >Acceder
          </b-button>
        </b-card>
      </p>
    </label>
  </b-card-group>
</template>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data() {
    return {
      categories: [],
    };
  },

  methods: {
    getCategories() {
      const path = Constants.API_URL + "categories/";

      axios
        .get(path)
        .then((response) => {
          this.categories = response.data.results;
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
