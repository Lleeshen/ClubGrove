<template>
  <div v-if="items">
  <b-card-group deck style="margin: 10px">
    <div v-for="item in currentPageItems">
      <Baseholder 
      v-bind:items="item"
      :isEvent="isEvent"
       style="margin-bottom: 30px"
       ></Baseholder>
    </div>
  </b-card-group>
  <b-pagination
      v-model="currentPage"
      :total-rows= "totalRows"
      :per-page="perPage"
    ></b-pagination>
</div>
</template>

<script>
// @ is an alias to /src
import Baseholder from '../components/Baseholder'
//calulated page from this https://stackoverflow.com/questions/52135382/bootstrap-vue-perpage-for-custom-columns-or-rows
export default {
  name: 'BaseholderPage',
  props: {items: {
      type: Array,
      default: [{}]
    },
    isEvent: 
    {
      type: Boolean,
      default: false
    }
   },
  components : {Baseholder},
  data() {
    return{
      perPage: 4,
      currentPage: 1,
      totalRows: 0,
      pagniated_items: {},
      nbPages: 0
    }
  },
  computed:
  {
    pageCount(){
      if(this.items != null)
      {
        let l = this.totalRows,
          s = this.perPage;
        return Math.floor(l , s);
      }
      return 0;
    },
    currentPageItems(){
      if(this.items != null)
      {
        let len = this.items.length;
        this.nbPages = 0;
        for(let i =0; i< len; i = i + this.perPage)
        {
          this.pagniated_items[this.nbPages] = this.items.slice(
            i, i+this.perPage);
          ++(this.nbPages);
        }
        return this.pagniated_items[this.currentPage -1];
      }
      return [];
    }
  },
  updated(){
    if(this.items)
    {
      this.totalRows = this.items.length;
    }
  }
}

</script>

<style scoped>
#searchBar {
  height: auto;
  background-color: #AFB781;
}

form {
  margin: 0 auto;
  padding: 15px 15px;
}

h2 {
  text-align: left;
  margin-left: 5%;
  margin-top: 20px;
}

.searchFormElt {
  margin: 0 10px 0 10px;
}

</style>