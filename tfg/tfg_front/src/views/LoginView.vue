<template>
  <b-container style="padding: 1rem">
    <h1 style="padding: 2rem">Iniciar sesión</h1>
    <b-row class="justify-content-center">
      <b-col lg="5" md="8">
        <b-card>
          <b-container>
            <b-row class="justify-content-center">
              <div class="forms-inputs mb-4">
                <span><b>- Correo</b></span>
                <input
                  class="label_margin"
                  type="text"
                  v-model="email"
                  v-bind:class="{
                    'form-control': true,
                    'is-invalid': !validEmail(email) && emailBlured,
                  }"
                  v-on:blur="emailBlured = true"
                />
                <div class="invalid-feedback">
                  Utiliza un correo electrónico válido
                </div>
              </div>
              <div class="forms-inputs mb-4">
                <span><b>- Contraseña</b></span>
                <input
                  class="label_margin"
                  autocomplete="off"
                  type="password"
                  v-model="password"
                  v-bind:class="{
                    'form-control': true,
                    'is-invalid': !validPassword(password) && passwordBlured,
                  }"
                  v-on:blur="passwordBlured = true"
                />
                <div class="invalid-feedback">
                  La contraseña debe tener más de 8 caracteres
                </div>
              </div>
            </b-row>

            <b-row style="margin-bottom: 1rem" class="justify-content-center">
              <b-col cols="8">
                <div style="margin-top: 1rem">
                  <b-button
                    v-on:click.stop.prevent="submit"
                    class="btn btn-dark w-100"
                    variant="primary"
                  >
                    Acceder
                  </b-button>
                </div>
                <div style="margin-top: 1rem">
                  <b-button
                    v-on:click.stop.prevent="logout"
                    class="btn btn-dark w-100"
                    variant="dark"
                  >
                    Cerrar sesión
                  </b-button>
                </div>
              </b-col>
            </b-row>
          </b-container>
        </b-card>
      </b-col>
    </b-row>

    <b-row
      style="margin-top: 2rem"
      class="justify-content-center"
      v-if="$store.state.isAuthenticated == false"
    >
      <p>
        ¿No te has registrado aún? ->
        <a class="custom-a" href="/register">Registro inicial</a>
      </p>
    </b-row>
  </b-container>
</template>

<style>
.label_margin {
  margin-top: 1rem;
}
.forms-inputs {
  text-align: left;
}
</style>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data: function () {
    return {
      email: "",
      emailBlured: false,
      valid: false,
      password: "",
      passwordBlured: false,
      submitted: false,
    };
  },

  methods: {
    validate: function () {
      this.emailBlured = true;
      this.passwordBlured = true;
      if (this.validEmail(this.email) && this.validPassword(this.password)) {
        this.valid = true;
      }
    },

    validEmail(email) {
      var re = /(.+)@(.+){2,}\.(.+){2,}/;
      if (re.test(email.toLowerCase())) {
        return true;
      }
    },

    validPassword(password) {
      if (password.length > 7) {
        return true;
      }
    },

    // Log-out
    logout() {
      if (this.$store.state.isAuthenticated) {
        const path = Constants.AUTH_URL + "token/logout/";

        axios
          .post(path, localStorage.getItem("token"), {
            headers: {
              Authorization: "Token " + localStorage.getItem("token"),
            },
          })
          .then((response) => {
            const token = response.data.auth_token;
            this.$store.commit("removeToken", token);
            localStorage.clear();

            this.$router.push("/");
          })
          .catch((error) => {
            console.log(error);
            localStorage.clear();
            this.$router.go();
          });
      }
    },

    // Submit -> Log-in
    submit() {
      this.validate();
      if (!this.$store.state.isAuthenticated) {
        if (this.valid) {
          const formData = {
            username: this.email,
            password: this.password,
            email: this.email,
          };

          const path = Constants.AUTH_URL + "token/login/";

          axios
            .post(path, formData)
            .then((response) => {
              const token = response.data.auth_token;
              const baseProfile = {
                userName: "",
                points: 0,
                isUpdated: false,
              };
              this.$store.commit("setToken", token);
              localStorage.setItem("token", token);
              localStorage.setItem("profile", JSON.stringify(baseProfile));

              axios.defaults.headers.common["Authorization"] = "Token " + token;

              this.$router.push("/");
            })
            .catch((error) => {
              if (!error.response) return;

              console.log(error);

              switch (error.response.status) {
                case 400:
                  if (
                    error.response.data.non_field_errors[0] &&
                    error.response.data.non_field_errors[0] ===
                      "Unable to log in with provided credentials."
                  ) {
                    alert(
                      "Credenciales erróneas. Intenta iniciar de sesión nuevamente."
                    );
                  }
                  break;

                case 401:
                  alert(
                    "Ups, ha ocurrido un error. Intenta iniciar de sesión nuevamente."
                  );
                  localStorage.clear();
                  this.$router.go();
                  break;

                default:
                  alert("Ups, ha ocurrido un error inesperado.");
                  localStorage.clear();
                  this.$router.go();
              }
            });
        }
      } else {
        alert(
          "Ya has iniciado sesión, prueba a cerrar sesión antes de continuar."
        );
      }
    },
  },
};
</script>
