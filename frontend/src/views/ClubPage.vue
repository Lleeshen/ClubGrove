<template>
  <div>
    {{item}}
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'clubPage',
  data() {
    return {
      //Replace this with actual club results
      item: null

    }
  },
  mounted() {
    var a = this.$route.params.name;
    var strin2 = 'http://localhost:5000/db/view/club/'.concat(a)
    console.log(strin2)
    axios
      .get(strin2)
      .then(response => {this.item = response.data;
       console.log(response) })
      .catch(error => {console.log(error)})
  }
}

</script>


</style>
