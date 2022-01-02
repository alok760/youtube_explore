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
    return <>
      <div className="card" >
        <div className="row no-gutters">
            <div className="col-sm-5">
                <img className="card-img" src="/images/defaultimg.png" alt="Suresh Dasari Card"/>
            </div>
            <div className="col-sm-7">
                <div className="card-body">
                    <h5 className="card-title">Suresh Dasari</h5>
                    <p className="card-text">Suresh Dasari is a founder and technical lead developer in tutlane.</p>
                    <a href="/something" className="btn btn-primary">View Profile</a>
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
