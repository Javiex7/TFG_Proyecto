<template>
  <!-- Category quizzes -->
  <b-row>
    <h3 class="text-start">
      Cuestionarios <i class="bi bi-question-circle"></i>
    </h3>
  </b-row>

  <b-card-group deck>
    <label v-for="quiz in quizzes" :key="quiz.id">
      <p style="margin: 1.5rem">
        <b-card style="max-width: 20rem" border-variant="secondary">
          <b-card-title :text="quiz.name" tag="h4" class="text-start" />

          <b-card-text :text="quiz.description" tag="p" class="text-start" />

          <b-button v-bind:href="'/quizzes/' + quiz.id" variant="secondary"
            >Acceder
          </b-button>
        </b-card>
      </p>
    </label>
  </b-card-group>
</template>

<script>
export default {
  props: {
    quizzes: null,
  },
};
</script>
