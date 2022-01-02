import { useEffect, useState } from "react";

import React from "react";
import axios from 'axios';

function Layout() {

  const [videoData, setVideoData] = useState([]);
  
  useEffect(() => {
    async function fetchData() {
      const response = await axios.get("http://localhost:8000/search");
      setVideoData(response.data);
      // debugger;
    }
    fetchData();
  }, [])

  function renderCard(video) {
    // debugger;
    const videoUrl = `https://www.youtube.com/watch?v=${video.pk}`
    return <>
      <div className="card my-2" style={{width: '70%'}}>
        <div className="row no-gutters">
            <div className="col-sm-5">
              <a href={videoUrl} target="_blank" rel="noreferrer"> <img className="card-img m-2" src={video.fields.thumbnail_url} alt="Suresh Dasari Card"/> </a>
            </div>
            <div className="col-sm-7">
                <div className="card-body">
                    <h5 className="card-title">{video.fields.title}</h5>
                    <p className="card-text">{video.fields.description}</p>
                    <a href={videoUrl} target="_blank" rel="noreferrer" className="btn btn-primary">View on Youtube </a>
                </div>
            </div>
        </div>
      </div>
    </>
  }

  function renderCards() {
    // debugger;
    return <>
      {videoData.map((video)=>renderCard(video))}
    </>;
  }

  
  return <>
<main role="main">

      <section className="jumbotron text-center">
        <div className="container">
          <h1 className="jumbotron-heading">Album example</h1>
          <p className="lead text-muted">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don't simply skip over it entirely.</p>
          <p>
            <a href="#" className="btn btn-primary my-2">Main call to action</a>
            <a href="#" className="btn btn-secondary my-2">Secondary action</a>
          </p>
        </div>
      </section>

      <div className="album py-5 bg-light">
        <div className="container">

          <div className="row">
            {videoData && renderCards()}
          </div>
        </div>
      </div>

    </main>
    </>;
}

export default Layout;
