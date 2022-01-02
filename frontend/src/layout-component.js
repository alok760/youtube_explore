import { useEffect, useState } from "react";

import CONSTANTS from "./constants";
import React from "react";
import axios from 'axios';

function Layout() {

  const [videoData, setVideoData] = useState([]);
  const [search, setSearch] = useState(null);
  const [sort, setSort] = useState('desc');
  const [input, setInput] = useState('');
  
  useEffect(() => {
    async function fetchData() {
      const params = {
        search: search,
        sort: sort
      }
      const response = await axios.get(CONSTANTS.apiUrl, {params: params});
      setVideoData(response.data);
    }
    fetchData();
  }, [search, sort])

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      setSearch(input);
    }
  }


  function renderCard(video) {
    const videoUrl = `https://www.youtube.com/watch?v=${video.pk}`
    return <>
      <div className="card my-2" style={{width: '100%'}}>
        <div className="row no-gutters">
            <div className="col-md-3 ">
              <a href={videoUrl} target="_blank" rel="noreferrer"> <img className="card-img m-2" src={video.fields.thumbnail_url} alt="youtube video description"/> </a>
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
    return <>
      {videoData.map((video)=>renderCard(video))}
    </>;
  }

  
  return <>
<main role="main">

      <section className="jumbotron py-3 text-center">
        <div className="container">
          <h1 className="jumbotron-heading">Youtube Video Search</h1>
          {/* <p className="lead text-muted">Search Education Related Videos Here</p> */}
          <div className="form-inline my-2 my-lg-0">
            <input className="form-control mr-sm-2 w-75 py-2"
              type="search"
              value={input}
              onInput={e => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Search Education Related Videos Here" aria-label="Search"
            />
            <button className="btn btn-outline-success my-2 my-sm-0" onClick={()=>setSearch(input)}> Search</button>
          </div>
        </div>
      </section>

      <div className="album py-3 bg-light">
        <div className="container">
          <div className="row">
            <div className="col-md-10">
              {videoData && renderCards()}
            </div>
            <div className="col text-center">
            <label for="sel1">Sort By:</label>
            <select class="form-control" onChange={e => setSort(e.target.value)} id="sel1">
              <option value="desc">Newest First</option>
              <option value="asc">Oldest First</option>
            </select>
            </div>
          </div>
        </div>
      </div>

    </main>
    </>;
}

export default Layout;
