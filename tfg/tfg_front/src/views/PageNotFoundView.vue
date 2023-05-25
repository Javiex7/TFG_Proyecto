<template>
  <b-container style="padding-top: 1rem">
    <div>
      <h1>404 - Página no encontrada</h1>
      <div style="margin: 1.5rem">
        <p>Lo sentimos, pero esta página no existe...</p>
        <p>Volvamos a la <a href="/">página principal</a></p>
      </div>
    </div>

    <div>
      <b-button v-b-modal.modal-1>Launch demo modal</b-button>

      <b-modal hide-backdrop id="modal-1" title="BootstrapVue">
        <p class="my-4">Hello from modal!</p>
      </b-modal>
    </div>

    <button @click="show = !show">Toggle</button>
    <Transition name="bounce">
      <p v-if="show" style="margin-top: 20px; text-align: center">
        Hello here is some bouncy text!
      </p>
    </Transition>
  </b-container>
</template>

<style scoped>
a {
  color: #51d990;
  font-weight: bold;
  text-decoration: none;
}

a:hover {
  color: #51d990;
  text-decoration: underline;
}

.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}
</style>

<script>
export default {
  data() {
    return { show: true };
  },
};
</script>
