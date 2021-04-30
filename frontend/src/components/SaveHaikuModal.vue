<template>
  <form action="">
    <div class="modal-card" style="width: 20rem">
      <header class="modal-card-head">
        <p class="modal-card-title">Save Haiku</p>
        <button
            type="button"
            class="delete"
            @click="$emit('close')"/>
      </header>

      <section class="modal-card-body">
        <b-field label="Pseudonym">
          <b-input
              type="text"
              :value="pseudonym"
              placeholder="Your pseudonym"
              required>
          </b-input>
        </b-field>
      </section>

      <section class="modal-card-body">
        <b-field label="Haiku rating">
          <b-rate custom-text="Haiku quality"
                  v-model="haikuRating"
                  spaced="true"
                  show-text="true"
                  icon="circle"
                  :texts="texts"
          ></b-rate>
        </b-field>
      </section>

      <footer class="modal-card-foot">
        <b-button
            label="Save"
            type="is-primary"
            @click="submitHaikuData"
        />
      </footer>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: "SaveHaikuModal",
  props: {
    "haikuText": String
  },
  data() {
    return {
      pseudonym: "Soaring Albatross",
      haikuRating: 3,
      texts: ['Very bad', 'Bad', 'Ok', 'Very good', 'Awesome'],
    }
  },
  methods: {
    submitHaikuData() {
      axios.post("http://localhost:8000/haiku/save", {
        "pseudonym": this.pseudonym,
        "rating": this.haikuRating,
        "haiku_text": this.haikuText
      })
      .then((response) => {
        if (response.data.status === 1) {
          this.$emit('close');
          this.$buefy.toast.open({
            duration: 3000,
            message: "Your Haiku was saved! Tune in later when the gallery page is up!",
            position: 'is-bottom',
            type: 'is-success'
          })
        } else {
          this.$emit('close');
          this.$buefy.toast.open({
            duration: 3000,
            message: "Something went wrong. :(",
            position: 'is-bottom',
            type: 'is-danger'
          })
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
