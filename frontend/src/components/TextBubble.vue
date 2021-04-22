<template>
  <div class="text-bubble">
  {{ text }}
  </div>
</template>

<script>
export default {
  name: "TextBubble",
  props: {
    "text": String
  },
  data() {
    return {

    }
  }
}
</script>

<style scoped lang="scss">

  .text-bubble {
    margin: 1rem;
    padding: 1rem;
    border: 1px solid $primary-color;
    border-radius: 5px;
    box-shadow: $accent-color 0px 2px 4px;
  }

</style>
