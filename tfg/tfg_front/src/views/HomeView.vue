<template>
  <b-container style="padding: 1rem">
    <b-row style="margin-top: 1rem">
      <!-- Introduction text -->
      <b-col lg="7">
        <b-row>
          <h3 class="text-start">Bienvenido a Histología práctica!</h3>
        </b-row>
        <b-row style="margin-top: 1rem">
          <p class="text-start">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </b-row>
        <b-row style="margin-top: 1rem">
          <b-col cols="1">
            <b-img v-bind="circleProp" rounded="circle" />
          </b-col>
          <b-col cols="11">
            <div class="ms-2 ms-md-0">
              <p class="text-start">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
            </div>
          </b-col>
        </b-row>
      </b-col>

      <!-- Main image -->
      <b-col lg="5" align-self="center" style="margin-top: 1rem">
        <b-row> </b-row>
        <b-img src="@/assets/main_page_image.jpg" fluid rounded="pill" />
      </b-col>
    </b-row>

    <b-row style="margin-top: 2rem">
      <ListCategories />
    </b-row>
  </b-container>
</template>

<script>
import ListCategories from "../components/categories/ListCategories";

export default {
  components: {
    ListCategories,
  },
  data() {
    return {
      circleProp: {
        blank: true,
        blankColor: "#51D990",
        width: 25,
        height: 25,
      },
    };
  },
};
</script>
