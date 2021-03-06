"""
Class of Linkage Groups
"""
from Data import Data


class LinkageGroup:
    LinkageGroups = dict()

    def __init__(self, id=None, name=None, markers=[], skeletonMarker=[], markerOrd=[], network=None):
        """
        Linkage group
        :param id: Linkage Group ID
        :param name: Linkage group name
        :param markers: list of markers that belong to this group
        :param skeletonMarker: list of skeleton markers
        :param markerOrd: list of markers
        :param network: network that linkage group belongs to
        """
        self.id = id
        self.name = name
        self.markers = markers
        self.skeletonMarker = skeletonMarker
        self.markerOrd = markerOrd
        self.network = network

    @staticmethod
    def create_linkages(linkageGroupsDict=dict()):
        for key in linkageGroupsDict:
            LinkageGroup.LinkageGroups[key] = LinkageGroup(linkageGroupsDict[key][0].id, key, linkageGroupsDict[key],[],[], None)

        Data.linkage_groups = LinkageGroup.LinkageGroups

