<template>
  <div>
    <div class="user-input-wrapper">
      <input
          type="text"
          class="user-input"
          placeholder="Blissful wind"
          v-model="userInput"
      >
    </div>
    <b-button
        type="is-info"
        @click="createNewHaiku"
    >
      Create Haiku
    </b-button>
    <div>
      {{generatedHaiku}}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "UserInput.vue",
  data() {
    return {
      "userInput": "",
      "generatedHaiku": ""
    }
  },
  methods: {
      createNewHaiku() {
        axios.post("http://localhost:8000/haiku/create", {
          "starter_words": this.userInput
        })
        .then((response) => {
          console.log(response);
          this.generatedHaiku = response.data.haiku;
        });
      }
    }
}
</script>

<style scoped lang="scss">
.user-input {
  padding: 0.5rem;
  margin: 1rem;
  font-size: 3rem;
  border: 0;
  text-align: center;
  border-bottom: 2px solid #333;
  transition: 0.25s;
  &:focus {
      outline: none;
      border-bottom: 2px solid red;
      transition: 0.25s;
    }
}
</style>
