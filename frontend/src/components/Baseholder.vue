<template>
  <div v-if="hasParams()">
    <b-card 
      style="width: 20rem" 
      class="text-center" 
      v-bind:header= "property.name"
      border-variant="dark"
      bg-variant="light">
    <b-card-text class="text-left">
    <b>Summary</b><br>
      {{property.description}}
        <div v-if= "hasEventParams()">
        Place: {{property.place}} <br>
        Start Time: {{property.starttime}} <br>
        End Time: {{property.starttime}}
        </div>
    </b-card-text>
    <div v-if= "!isEvent">
    <b-button v-bind:to="link">To club Page</b-button>
    </div>
  </b-card>
    
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Baseholder',
  props: ['items', 'isEvent'],
  data: function() {
    return {
      property: this.items
    }
  },
  methods:
  {
      hasParams: function() 
      {
          if(this.property && this.property.name
            && this.property.description)
            {
                return true;
            }
            return false;
      },
      hasEventParams: function() 
      {
          if(this.property && this.property.place
            && this.property.starttime && this.property.endtime)
            {
                return true;
            }
            return false;
      }

  },
  computed:
  {
      link: function()
      {
          return "club/" + this.items.name;
      }

  }
}

</script scoped>
.card {
  border: 2px;
}
</style>