<template>
  <b-container style="padding-top: 1rem; padding-bottom: 1rem">
    <b-card v-if="this.startedAttempt === false" pill variant="secondary">
      {{ userQuiz.quiz.description }}
    </b-card>

    <b-row v-else
      ><h2 class="text-start">
        Intento {{ userQuiz.tries }}/{{ userQuiz.quiz.max_tries }}
      </h2>
    </b-row>

    <b-row
      v-if="this.startedAttempt === false"
      style="margin-top: 1rem"
      pill
      variant="danger"
    >
      <h2>Intento {{ userQuiz.tries }}/{{ userQuiz.quiz.max_tries }}</h2>
      <h2>{{ questionsNumber }} preguntas</h2>
    </b-row>

    <b-container v-else style="margin-top: 1rem">
      <!-- Question box/card -->
      <div class="questionBox" id="app">
        <!-- Transition animation -->
        <b-row class="justify-content-md-center">
          <b-col lg="7">
            <b-card>
              <transition mode="out-in" name="slide-fade">
                <b-container :key="questionIndex">
                  <!-- Quiz elements -->
                  <div
                    class="questionContainer"
                    v-if="questionIndex < userQuiz.quiz.questions.length"
                    v-bind:key="questionIndex"
                  >
                    <b-card-header style="margin-bottom: 2rem">
                      <!-- Quiz title/name -->
                      <h2 style="margin-top: 1rem" class="title is-6">
                        {{ userQuiz.quiz.name }}
                      </h2>
                      <!-- Progress bar -->
                      <div class="progressContainer">
                        <progress
                          class="border-radius: 1rem; overflow: hidden; border:none;"
                          :value="
                            (questionIndex / userQuiz.quiz.questions.length) *
                            100
                          "
                          max="100"
                        >
                          {{
                            (questionIndex / userQuiz.quiz.questions.length) *
                            100
                          }}%
                        </progress>
                        <p>
                          {{
                            (questionIndex / userQuiz.quiz.questions.length) *
                            100
                          }}% completo
                        </p>
                      </div>
                    </b-card-header>

                    <!-- Current question -->
                    <h3 class="titleContainer title">
                      {{ userQuiz.quiz.questions[questionIndex].question }}
                    </h3>

                    <b-img
                      v-if="userQuiz.quiz.questions[questionIndex].image"
                      :src="userQuiz.quiz.questions[questionIndex].image"
                      rounded="pill"
                      pointer-events="none"
                      width="300rem"
                      height="300rem"
                      class="quiz-image"
                    />

                    <!-- Question options -->
                    <b-form-group buttons v-slot="{ ariaDescribedby }">
                      <b-form-radio-group
                        buttons
                        stacked
                        button-variant="outline-primary"
                      >
                        <b-form-radio
                          style="margin-top: 1rem"
                          v-model="selectedOption"
                          value="A"
                          :aria-describedby="ariaDescribedby"
                          >a.
                          {{ userQuiz.quiz.questions[questionIndex].option_a }}
                        </b-form-radio>
                        <b-form-radio
                          style="margin-top: 1rem"
                          v-model="selectedOption"
                          value="B"
                          :aria-describedby="ariaDescribedby"
                          >b.
                          {{ userQuiz.quiz.questions[questionIndex].option_b }}
                        </b-form-radio>
                        <b-form-radio
                          style="margin-top: 1rem"
                          v-model="selectedOption"
                          value="C"
                          :aria-describedby="ariaDescribedby"
                          >c.
                          {{ userQuiz.quiz.questions[questionIndex].option_c }}
                        </b-form-radio>
                        <b-form-radio
                          style="margin-top: 1rem"
                          v-model="selectedOption"
                          value="D"
                          :aria-describedby="ariaDescribedby"
                          >d.
                          {{ userQuiz.quiz.questions[questionIndex].option_d }}
                        </b-form-radio>
                      </b-form-radio-group>
                    </b-form-group>

                    <!-- Footer with navigation -->
                    <b-card-footer style="margin-top: 2rem">
                      <b-row
                        class="justify-content-md-center"
                        style="margin-top: 1rem; margin-bottom: 1rem"
                      >
                        <b-col v-if="questionIndex >= 1">
                          <!-- Previous question button -->
                          <b-button v-on:click="prev()" variant="back"
                            >Atrás
                          </b-button>
                        </b-col>

                        <b-col>
                          <!-- Next question button -->
                          <b-button
                            v-if="
                              questionIndex < userQuiz.quiz.questions.length - 1
                            "
                            variant="primary"
                            v-on:click="next()"
                          >
                            Siguiente
                          </b-button>
                          <b-button
                            v-else
                            variant="secondary"
                            v-on:click="next()"
                          >
                            Finalizar
                          </b-button>
                        </b-col>
                      </b-row>
                    </b-card-footer>
                  </div>

                  <!-- Quiz results -->
                  <div
                    v-if="questionIndex >= userQuiz.quiz.questions.length"
                    v-bind:key="questionIndex"
                    class="quizCompleted has-text-centered"
                  >
                    <h2 class="title">Intento finalizado</h2>
                    <h3 style="margin-top: 1rem; margin-bottom: 1rem">
                      Respuestas correctas:
                      <span
                        class="incorrectAnswers"
                        :class="{
                          correctAnswers: score >= questionsNumber,
                        }"
                        >{{ score }}/{{ userQuiz.quiz.questions.length }}
                      </span>
                    </h3>

                    <b-container v-if="obtainedPoints > 0">
                      <p>
                        Debido a que has mejorado tu puntuación has obtenido:
                      </p>
                      <p class="correctAnswers">
                        +{{ obtainedPoints }}
                        puntos
                      </p>
                    </b-container>

                    <b-button
                      v-bind:href="'/quizzes/' + userQuiz.quiz.id"
                      variant="secondary"
                      >Volver
                    </b-button>
                  </div>
                </b-container>
              </transition>
            </b-card>
          </b-col>
        </b-row>
      </div>
    </b-container>

    <h3 style="margin-top: 2rem" v-if="this.startedAttempt === false">
      Puntuación obtenida:
      <h3
        class="incorrectAnswers"
        :class="{
          correctAnswers: userQuiz.correct_answers >= questionsNumber,
        }"
      >
        {{ userQuiz.correct_answers }}/{{ questionsNumber }} puntos
      </h3>
    </h3>

    <b-button
      v-if="
        this.startedAttempt === false &&
        userQuiz.tries < userQuiz.quiz.max_tries
      "
      style="margin-top: 1rem"
      @click="startQuizAttempt"
      variant="secondary"
      >Empezar nuevo intento
    </b-button>

    <b-badge
      v-else-if="this.startedAttempt === false"
      style="margin-top: 1rem; padding: 1rem"
      variant="secondary"
      pill
      >Intentos máximos alcanzados...
    </b-badge>
  </b-container>
</template>

<style scoped>
.quiz-image {
  border: 2px solid #555;
  pointer-events: none;
}
.incorrectAnswers {
  color: rgb(240, 145, 28);
  font-weight: bold;
}
.correctAnswers {
  color: #51d990;
  font-weight: bold;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.2s ease-in;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
}
</style>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data() {
    return {
      quizId: {},
      userQuiz: {
        quiz: {},
      },
      questionsNumber: "",
      startedAttempt: false,
      questionIndex: 0,
      selectedOption: "",
      userResponses: [],
      score: 0,
      obtainedPoints: 0,
    };
  },

  methods: {
    getUserQuiz(quizId) {
      const path = Constants.API_URL + "quizzes/" + parseInt(quizId) + "/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then((response) => {
          this.userQuiz = response.data;
          this.questionsNumber = this.userQuiz.quiz.questions.length;
        })
        .catch((error) => {
          if (error.response && error.response.status == 401) {
            this.$router.push({ path: "/login", replace: true });
          }
        });
    },
    startQuizAttempt() {
      if (!this.quizId) return;

      const path =
        Constants.API_URL +
        "quizzes/" +
        parseInt(this.quizId) +
        "/startAttempt/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .patch(path, {}, { headers })
        .then((response) => {
          if (response.status == 200) {
            this.userQuiz.tries++;
            this.startedAttempt = true;
            this.userResponses = Array(this.userQuiz.qui.questions.length).fill(
              null
            );
          }
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response);
          }
        });
    },

    restartQuiz() {
      this.questionIndex = 0;
      this.userResponses = Array(this.userQuiz.quiz.questions.length).fill(
        null
      );
    },

    next() {
      if (this.questionIndex < this.userQuiz.quiz.questions.length) {
        this.userResponses[this.questionIndex] = {
          id: this.userQuiz.quiz.questions[this.questionIndex].id,
          correct_option: this.selectedOption,
        };
        if (this.userResponses[this.questionIndex + 1]) {
          this.selectedOption =
            this.userResponses[this.questionIndex + 1].correct_option;
        } else {
          this.selectedOption = "";
        }

        this.questionIndex++;

        if (this.questionIndex === this.userQuiz.quiz.questions.length) {
          this.calculateScore();
        }
      }
    },

    prev() {
      if (this.userQuiz.quiz.questions.length > 0) {
        this.userResponses[this.questionIndex] = {
          id: this.userQuiz.quiz.questions[this.questionIndex].id,
          correct_option: this.selectedOption,
        };

        if (this.userResponses[this.questionIndex - 1]) {
          this.selectedOption =
            this.userResponses[this.questionIndex - 1].correct_option;
        } else {
          this.selectedOption = "";
        }

        this.questionIndex--;
      }
    },

    calculateScore() {
      const path =
        Constants.API_URL +
        "quizzes/" +
        parseInt(this.userQuiz.quiz.id) +
        "/finishAttempt/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      const parameters = { userResponses: this.userResponses };

      axios
        .patch(path, parameters, { headers })
        .then((response) => {
          this.score = response.data.correct_answers;
          this.obtainedPoints = response.data.points;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.quizId = this.$route.params.quizId;

    if (this.$store.state.isAuthenticated) {
      this.getUserQuiz(this.quizId);
    } else {
      this.$router.push({ path: "/login", replace: true });
    }
  },
};
</script>
