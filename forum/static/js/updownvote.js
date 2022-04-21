const updownvote_topic = async (topic_id, action) => {
    const data = {action}
    const result = await fetch(`topic/${topic_id}/updownvote/`,
        {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    )
    console.log(result)
    const text = await result.text()
    console.log(text)
    if (result.status === 200) {
        document.getElementById(`topic_votes_${ topic_id }`).innerHTML=text;
    } else {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: text,
        })
    }
}