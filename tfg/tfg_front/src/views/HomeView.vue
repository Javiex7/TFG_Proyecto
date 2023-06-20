<template>
  <b-container style="padding: 1rem">
    <b-row style="margin-top: 1rem">
      <!-- Introduction text -->
      <b-col lg="7">
        <b-row>
          <h3 class="text-start">¡Bienvenido a Histología práctica!</h3>
        </b-row>
        <b-row style="margin-top: 1rem">
          <p class="text-start">
            A través de esta aplicación podrás poner en práctica tus
            conocimientos y habilidades en el campo de la histología a través de
            contenido adicional en forma de tests y acceso a muestras
            histológicas. Revisa con tu profesor/encargado las recompensas,
            normas y elementos asociados a la evaluación y uso de la aplicación.
          </p>
        </b-row>
        <b-row style="margin-top: 1rem">
          <b-col cols="12" class="text-start">
            <b-button
              class="custom-button"
              type="link"
              href="/general-practice"
              variant="secondary"
              >Práctica general
            </b-button>
          </b-col>
        </b-row>
        <b-row style="margin-top: 3rem; margin-bottom: 2rem">
          <b-col cols="1">
            <b-img v-bind="circleProp" rounded="circle" />
          </b-col>
          <b-col cols="11">
            <div class="ms-2 ms-md-0">
              <p class="text-start">
                Realiza cuestionarios para <u>ganar puntos</u> y úsalos para
                poder acceder a <u>muestras adicionales</u> y otras recompensas.
              </p>
            </div>
          </b-col>
        </b-row>
      </b-col>

      <!-- Main image -->
      <b-col lg="5" align-self="center" style="margin-top: 1rem">
        <b-img src="@/assets/main_page_image.jpg" fluid rounded="pill" />
      </b-col>
    </b-row>

    <b-row style="margin-top: 2rem">
      <ListCategories />
    </b-row>
  </b-container>
</template>

<style scoped>
.custom-button {
  width: 12rem;
  border-radius: 0.75rem;
}
</style>

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
