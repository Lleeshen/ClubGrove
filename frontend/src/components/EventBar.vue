<template>
<b-container fluid style="border: .5px solid grey; margin: 10px" >
    <b-row class = "row align-items-center" style="background: antiquewhite">
      <b-col>
        <h3> {{ name }} Events </h3>
      </b-col>
      <b-col cols="8" class= "border border-dark bg-SCU">
        <b-card-group v-if="items && items.length > 0" style="margin: 10px">
      <div v-for="item in lessEvent" :key="item.name">
        <Baseholder 
            v-bind:items="item" 
            isEvent="true">
        </Baseholder>
      </div>
      </b-card-group>
      <b-card-group class ="h-100" v-else >
        <b-card 
      style="width: 20rem; height: 10rem"  
      border-variant="dark"
      bg-variant="light"
      align= "center">
      <b-card-text class="text-center">
      <p>There are no events</p>
      </b-card-text>
      </b-card>
      </b-card-group>
      </b-col>
      <b-col>
      <b-button v-bind:to="eventLink" class="mt-auto">More Club events</b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// @ is an alias to /src
import Baseholder from '../components/Baseholder'
export default {
  name: 'EventBar',
  components: {Baseholder},
  data() {
    return {
      validClub: false,
      fields: [
        {key:'name', label: 'Event Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
      items: null,
      clubName: this.name
    }
  },
  mounted() {
    if(this.clubName)
    {
        this.$axios
        .post('http://localhost:5000/api/getEvents',{'nm': this.clubName})
        .then(response => {this.items = response.data;
        console.log(response.data) })
        .catch(error => {console.log(error)})
    }
  },
  computed:
  {
      eventLink: function()
      {
          return this.name.concat("/events");
      },
      lessEvent: function()
      {
        if(this.items)
        {
          return this.items.slice(0,3);
        }
        return [];
      }

  },
  props: ['name']
}

</script>

<style scoped>
.border{
  border-width: 1px !important;
}

.bg-SCU
{
  background-color: #AFB781;
}
</style>