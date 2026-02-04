"""::map_stream.py"""
"""copyright ( c ) @ Hunter M."""

MAP_STREAM_VERSION = "0.0.1"

MAP_NAME = str
MAP_EXTENSION = ".reqmap1"

MAP_STREAM_DBG = "::DEBUG_STREAM"

class MapStream:
  map_size = int
  map_date = "__DATE__"
  map_name = MAP_NAME
  map_extension = MAP_EXTENSION
  stream_line_number = [int]
  map_line_section = [str][stream_line_number]

  """@map variables"""
  map_brush_count = [int]
  map_face_count = [int]
  map_plane_count = [int]
  map_caulk_count = [int]
  map_clip_count = [int]
  map_texdef_count = [int]
  map_entity_count = [int]
  map_node_count = [int]

  def streamGetMapNodeCount( self ):
    return self.map_node_count

  def streamGetMapEntityCount( self ):
    return self.map_entity_count

  def streamGetMapTexdefCount( self ):
    return self.map_texdef_count
  
  def streamGetMapClipCount( self ):
    return self.map_clip_count
  
  def streamGetMapCaulkCount( self ):
    return self.map_caulk_count
  
  def streamGetMapFaceCount( self ):
    return self.map_face_count

  def streamGetMapPlaneCount( self ):
    return self.map_plane_count
  
  def streamGetMapBrushCount( self ):
    return self.map_brush_count

  def streamGetMapExtension( self ):
    return self.map_extension

  def streamGetMapName( self ):
    return self.map_name
