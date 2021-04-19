<template>
  <div class="vertically-centered">
    <div class="user-input-wrapper">
      <input
          v-if="showInput"
          type="text"
          class="user-input"
          placeholder="Blissful wind"
          v-model="userInput"
      >
    </div>
    <br>
    <b-button
        id="create-haiku-button"
        v-if="userInput&&showInput"
        @click="createNewHaiku"
    >
      Create
    </b-button>
    <Haiku v-if="userInput" :content="userInput"></Haiku>
  </div>
</template>

<script>
import axios from 'axios';
import Haiku from "@/components/Haiku";

export default {
  name: "UserInput.vue",
  components: {
    "Haiku": Haiku
  },
  data() {
    return {
      userInput: "",
      showInput: true,
    }
  },
  methods: {
      createNewHaiku() {
        this.showInput = false;
        axios.post("http://localhost:8000/haiku/create", {
          "starter_words": this.userInput
        })
        .then((response) => {
          this.userInput = response.data.haiku;
          console.log(response);
        });
      }
    }
}
</script>

<style scoped lang="scss">
.user-input {
  padding: 0.5rem;
  margin-top: 10rem;
  font-size: 3rem;
  border: 0;
  text-align: center;
  border-bottom: 3px solid $primary-color;
  transition: 0.3s;
  background-color: transparent;
  font-weight: 100;
  &:focus {
      outline: none;
      border-bottom: 3px solid $accent-color;
      transition: 0.4s;
    }
}

#create-haiku-button {
  border: 1px solid $accent-color;

}
</style>
