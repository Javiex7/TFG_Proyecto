<template>
  <div class="container mt-5">
    <span><h1>Iniciar sesión</h1></span>
    <div class="row d-flex justify-content-center">
      <div class="col-md-6">
        <div class="card px-5 py-5">
          <div class="form-data" v-if="!submitted">
            <div class="forms-inputs mb-4">
              <span><b>- Correo</b></span>
              <input
                class="label_margin"
                autocomplete="off"
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
            <div class="mb-3">
              <button
                v-on:click.stop.prevent="submit"
                class="btn btn-dark w-100"
              >
                Acceder
              </button>
            </div>
            <div class="mb-3">
              <button
                v-on:click.stop.prevent="logout"
                class="btn btn-dark w-100"
              >
                Log out
              </button>
            </div>
          </div>
          <div class="success-data" v-else>
            <div class="text-center d-flex flex-column">
              <i class="bx bxs-badge-check"></i>
              <span class="text-center fs-1"
                >You have been logged in <br />
                Successfully</span
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <nav>
    <p>
      <router-link v-on:click.stop.prevent="logout" to="/register">
        Registro inicial
      </router-link>
    </p>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  data: function () {
    return {
      email: "",
      emailBlured: false,
      valid: false,
      submitted: false,
      password: "",
      passwordBlured: false,
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

    validEmail: function (email) {
      var re = /(.+)@(.+){2,}\.(.+){2,}/;
      if (re.test(email.toLowerCase())) {
        return true;
      }
    },

    validPassword: function (password) {
      if (password.length > 7) {
        return true;
      }
    },

    logout: function () {
      if (this.$store.state.isAuthenticated) {
        const path = "http://localhost:8000/auth/token/logout/";

        axios
          .post(path, localStorage.getItem("token"), {
            headers: {
              Authorization: "Token " + localStorage.getItem("token"),
            },
          })
          .then((response) => {
            console.log("LOG OUT ", response.data);

            const token = response.data.auth_token;
            this.$store.commit("removeToken", token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;

            localStorage.removeItem("token", token);

            this.$router.push("/");
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },

    submit: function () {
      this.validate();
      if (!this.$store.state.isAuthenticated) {
        if (this.valid) {
          const formData = {
            username: this.email,
            password: this.password,
            email: this.email,
          };

          const path = "http://localhost:8000/auth/token/login/";

          axios
            .post(path, formData)
            .then((response) => {
              console.log("LOG IN", response.data);

              const token = response.data.auth_token;
              this.$store.commit("setToken", token);

              axios.defaults.headers.common["Authorization"] = "Token " + token;

              localStorage.setItem("token", token);

              this.$router.push("/");
            })
            .catch((error) => {
              console.log(error);
            });
        }
      } else {
        this.$router.push("/");
      }
    },
  },
};
</script>

<style>
.label_margin {
  margin-top: 1rem;
}
.forms-inputs {
  text-align: left;
}
</style>
