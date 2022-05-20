<template>
  <div>
    <v-pagination
      v-model="page"
      :length="6"
    ></v-pagination>
  </div>
</template>

<script>
export default {
  name: 'reviewDetail',
  data () {
      return {
        page: 1,
      }
    },
}
</script>

<style>

</style>