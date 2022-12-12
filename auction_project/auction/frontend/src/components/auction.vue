
<template>
  <div class="mainContainer">

    <div class="input-group mb-3 search">
      <input id="searchBar" type="text" class="form-control" placeholder="Search" @keyup.enter="searchItems">
      <button @click="searchItems" class="btn btn-outline-secondary" type="button">Search</button>
    </div>

    <ItemComponent v-for="item in items" :item="item" />
  </div>

</template>


<script>
import ItemComponent from './ItemComponent.vue';

export default {
  components: {
    ItemComponent,
  },

  data() {
    return {
      items: [],
    };
  },
  async mounted() {
    let response = await fetch("http://127.0.0.1:8000/api/available/");
    let data = await response.json();
    this.items = data.items;

  },

  methods: {
    async fetchItems(query = "") {
      let response;

      if (query == "")
        response = await fetch("http://127.0.0.1:8000/api/available/");
      else
        response = await fetch("http://127.0.0.1:8000/api/available/" + query + "/");

      let data = await response.json();
      this.items = data.items;
    },

    async searchItems() {
      let query = document.getElementById('searchBar').value;
      this.fetchItems(query);
    }
  },

}

</script>

<style scoped>
.search {
  margin-left: 5em;
  margin-right: 5em;
  margin-top: 2em;
}

.search button {
  background-color: green;
  color: white;
}

.mainContainer {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>