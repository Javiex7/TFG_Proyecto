<template>
  <b-container style="padding-top: 2rem">
    <b-row style="padding-bottom: 2rem">
      <h2 class="text-start">Pack - {{ packDetail.name }}</h2>
    </b-row>

    <b-container v-if="!packDetail.purchased && packDetail.images">
      <h2>Todavía no has adquirido este paquete, ¿quieres comprarlo?</h2>
      <h3 style="padding-top: 1.5rem">
        <span class="highlightText">
          {{ packDetail.images.length }} imágenes disponibles
        </span>
        / <span class="warningText"> {{ packDetail.price }} puntos </span>
      </h3>

      <b-button
        v-if="!modalShow"
        @click="toggleModal"
        style="margin-top: 1.5rem"
      >
        Comprar pack
      </b-button>

      <b-container
        style="margin-top: 1.5rem"
        v-if="modalShow"
        class="modalCard"
      >
        <b-row>
          <b-col>
            <b-card>
              Actualmente tienes
              <span class="highlightText">
                {{ $root.userProfile.points }}
              </span>
              puntos, al comprar el paquete te quedarás con
              <span
                class="warningText"
                :class="{
                  highlightText:
                    $root.userProfile.points - packDetail.price >= 0,
                }"
                >{{ $root.userProfile.points - packDetail.price }}
              </span>
              puntos

              <b-card-body>
                <b-button @click="toggleModal" class="card-link" variant="dark"
                  >Cancelar
                </b-button>
                <b-button @click="buyPack" class="card-link" variant="primary"
                  >Ok!
                </b-button>
              </b-card-body></b-card
            >
          </b-col>
        </b-row>
      </b-container>
    </b-container>

    <b-container v-else>
      <b-card-group deck>
        <label v-for="image in packDetail.images" :key="image.id">
          <p style="margin: 1.5rem">
            <b-card
              :img-alt="image.name"
              :img-src="image.image"
              img-top
              style="max-width: 20rem"
              border-variant="secondary"
            >
              <b-card-title :text="image.name" tag="h5" />
            </b-card>
          </p>
        </label>
      </b-card-group>
    </b-container>
  </b-container>
</template>

<style scoped>
.modalCard {
  position: absolute;
  width: 20rem;
  z-index: 100;
  left: 50%;
  transform: translate(-50%);
}
</style>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  data() {
    return {
      modalShow: false,
      packId: {},
      packDetail: {},
      serverURL: Constants.BASE_URL,
    };
  },

  methods: {
    getPointPackDetail() {
      const path =
        Constants.API_URL + "point-packs/" + parseInt(this.packId) + "/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then((response) => {
          this.packDetail = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    toggleModal() {
      this.modalShow = !this.modalShow;
    },

    notPointsAlert() {
      alert("No tienes puntos suficientes para comprar este paquete...");
    },

    buyPack() {
      // Confirm the user can make the purchase
      if (this.$root.userProfile.points < this.packDetail.price) {
        this.notPointsAlert();
        this.toggleModal();
        return;
      }
      const path =
        Constants.API_URL +
        "point-packs/" +
        parseInt(this.packId) +
        "/buyPointPack/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then(() => {
          this.$root.updateUserInfo();
          this.$router.go();
        })
        .catch((error) => {
          if (error.response && error.response.status == 401) {
            localStorage.clear();
            this.$router.push({ path: "/login", replace: true });
          }
        });
    },
  },

  created() {
    this.packId = this.$route.params.packId;

    if (this.$store.state.isAuthenticated) {
      this.getPointPackDetail(this.packId);
    } else {
      localStorage.clear();
      this.$router.push({ path: "/login", replace: true });
    }
  },
};
</script>
